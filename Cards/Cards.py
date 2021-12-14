import math

import pygame
from Utils.Settings import Settings
import copy


def _rotate_in_place(image, top_left, degree):
    rotated_image = pygame.transform.rotozoom(image, degree, 1)
    rotated_rect = rotated_image.get_rect(center=image.get_rect(topleft=top_left).center)
    return rotated_image, rotated_rect


class Cards:

    def __init__(self, display, surface, value, suit, front_image, back_image):

        # The screen
        self.display = display
        self.surface = surface
        # Value of the card
        self.value = value
        # Suit of the card
        self.suit = suit
        # Front image of the card
        self.front_image = pygame.image.load(front_image)
        # Back image of the card
        self.back_image = pygame.image.load(back_image)

        self.settings = Settings()

        # Card size
        self.width = 100
        self.height = 150

        # We will default the size of the card to be 100, 150. We will be able
        # to scale it when dealing.
        self.front_image = pygame.transform.scale(self.front_image, (self.width, self.height))
        self.back_image = pygame.transform.scale(self.back_image, (self.width, self.height))

        # Opponent card or User card
        # We will make it default to true, so all cards will be dealt
        # face up
        self.front = True

        # Card Location
        self.x = -200
        self.y = -200

        # If a player has clicked on this card
        self.chosen = False

        # This boolean determines whether this card is in play (ie whether it is in the opponent's or player's hand)
        # This is to help with collision. If it is not in the player's hand, then the player should
        # not be able to click on the card
        self.in_play = False

        # rect used to handle clicking and collision
        self.rect_card = pygame.Rect(self.x, self.y, self.width, self.height)
        # rect used to calculate the area that is blocked by the card above
        self.rect_blocked = pygame.Rect(0, 0, 0, 0)

    # Move the card to a different location
    # If we are moving the card to the shuffle position, we will make it appear
    # instantly. If shuffle is true, then we are moving it to the shuffle
    # position. If it is false, we are dealing, playing, which will have a smooth position.
    # We have to move the image and the rectangle at the same time.
    def move(self, x, y, shuffle=False):
        x_distance = x - self.x
        y_distance = y - self.y

        x_direction = "positive" if (x_distance > 0) else "negative"
        y_direction = "positive" if (y_distance > 0) else "negative"

        # We save whether it is negative, we want the distance to be positive.
        if x_direction == "negative":
            x_distance *= -1
        if y_direction == "negative":
            y_distance *= -1

        if x_distance != 0 and y_distance != 0:
            slope = math.floor(y_distance / x_distance)
        else:
            slope = 0

        # If it is not a move to shuffle position, then we want to move it incrementally.
        # If it is a  shuffle move, then we can instantly move it.
        if not shuffle:
            while x_distance != 0 or y_distance != 0:
                if x_distance == 0:
                    if y_direction == "negative":
                        self.y += -1
                        y_distance -= 1
                    else:
                        self.y += 1
                        y_distance -= 1

                elif y_distance == 0:
                    if x_direction == "negative":
                        self.x += -1
                        x_distance -= 1
                    else:
                        self.x += 1
                        x_distance -= 1

                else:
                    if x_direction == "negative":
                        self.x += -1
                        x_distance -= 1
                    else:
                        self.x += 1
                        x_distance -= 1

                    if y_direction == "negative":
                        self.y += -1 * slope
                        y_distance -= slope
                    else:
                        self.y += slope
                        y_distance -= slope

                self.draw(still_drawing=True, is_front=self.front)

        else:
            self.x = x
            self.y = y
            self.draw(False, self.front)

        self.draw(is_front=self.front)

        self.update_card_collision(self.x, self.y)

    # Draw method. Blit the image, and move the rect to the x, y position
    def draw(self, still_drawing=False, is_front=True):
        if self.front and is_front:
            if still_drawing:
                temp_surface = copy.copy(self.surface)
                temp_surface.blit(self.front_image, (self.x, self.y))
                self.update_draw(permanent=False, surface=temp_surface)
            else:
                self.surface.blit(self.front_image, (self.x, self.y))
                self.update_draw(permanent=True)
        else:
            if still_drawing:
                temp_surface = copy.copy(self.surface)
                temp_surface.blit(self.back_image, (self.x, self.y))
                self.update_draw(permanent=False, surface=temp_surface)
            else:
                self.surface.blit(self.back_image, (self.x, self.y))
                self.update_draw(permanent=True)

    def draw_rotation(self, image, place, permanent=False):
        if not permanent:
            temp_surface = copy.copy(self.surface)
            temp_surface.blit(image, place)
            self.update_draw(permanent=False, surface=temp_surface)
        else:
            self.surface.blit(image, place)
            self.update_draw(permanent=True)

    # Update draw
    def update_draw(self, permanent=False, surface=None):
        if not permanent:
            self.display.fill(self.settings.bg_color)
            self.display.blit(surface, (0, 0))
        else:
            self.display.fill(self.settings.bg_color)
            self.display.blit(self.surface, (0, 0))
        pygame.display.flip()

    def reset_surface(self):
        self.display.fill(self.settings.bg_color)

    # Method to update the visibility of the card
    def update_vis(self, boolean):
        self.front = boolean

    # Method to rotate the card smoothly
    def rotate(self, degrees, is_front=True):
        is_positive = True if degrees >= 0 else False

        if not is_positive:
            new_degree = degrees * -1
        else:
            new_degree = degrees

        temp_image = self.front_image.copy() if is_front else self.back_image.copy()
        degree = 2

        while new_degree > 0:
            if is_positive:
                rotated_image, new_rect = _rotate_in_place(temp_image, (self.x, self.y), degree)
                self.draw_rotation(image=rotated_image, place=new_rect.topleft)

                temp_image = self.front_image.copy() if is_front else self.back_image.copy()
            else:
                rotated_image, new_rect = _rotate_in_place(temp_image, (self.x, self.y), -1 * degree)
                self.draw_rotation(rotated_image, new_rect.topleft)

                temp_image = self.front_image.copy() if is_front else self.back_image.copy()

            new_degree -= 2
            degree += 2

            if new_degree == 0:
                if is_front:
                    self.front_image = rotated_image
                else:
                    self.back_image = rotated_image

        self.draw(is_front=is_front)

    # Method to get the Width
    def get_width(self):
        return self.width

    # Method to get the Height
    def get_height(self):
        return self.height

    # Return the current position of the card
    def cur_pos(self):
        return self.x, self.y

    # Change the status of the chosen status of this card
    def change_chosen(self, boolean):
        self.chosen = boolean

    # return the status of whether a card is chosen
    def get_chosen(self):
        return self.chosen

    # Change the status of the in play instance
    def change_in_play(self, boolean):
        self.in_play = boolean

    # return the status of the in play instance
    def get_in_play(self):
        return self.in_play

    def update_card_collision(self, x, y):
        self.rect_card.update(x, y, self.width, self.height)

    def update_card_block_area(self, x, y, width, height):
        self.rect_blocked.update(x, y, width, height)

    def handle_selected(self, mouse_x, mouse_y):
        return self.rect_card.collidepoint((mouse_x, mouse_y)) and not \
            self.rect_blocked.collidepoint((mouse_x, mouse_y))

    def get_suit(self):
        return self.suit

    def get_value(self):
        return self.value
