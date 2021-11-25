import pygame


def _rotate_in_place(surface, top_left, angle):
    rotated_image = pygame.transform.rotozoom(surface, angle, 1)
    new_rect = rotated_image.get_rect(center=surface.get_rect(topLeft=top_left).center)
    return rotated_image, new_rect


class Cards:

    def __init__(self, win, value, suit, front_image, back_image):

        # The screen
        self.screen = win
        # Value of the card
        self.value = value
        # Suit of the card
        self.suit = suit
        # Front image of the card
        self.front_image = pygame.load(front_image)
        # Back image of the card
        self.back_image = pygame.load(back_image)

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
    def move(self, x, y, shuffle):
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
            slope = y_distance/x_distance
        else:
            slope = 0

        # If it is not a move to shuffle position, then we want to move it incrementally.
        # If it is a  shuffle move, then we can instantly move it.
        if not shuffle:
            while x_distance != 0 or y_distance != 0:
                if x_distance == 0:
                    if y_direction == "negative":
                        self.y += -1
                    else:
                        self.y += 1

                elif y_distance == 0:
                    if x_direction == "negative":
                        self.x += -1
                    else:
                        self.x += 1

                else:
                    if x_direction == "negative":
                        self.x += -1
                    else:
                        self.y += -1 * slope

                    if y_direction == "positive":
                        self.y += -1 * slope
                    else:
                        self.y += slope

                self.draw(self.front)
        else:
            self.x = x
            self.y = y

        self.update_card_collision(self.x, self.y)

    # Draw method. Blit the image, and move the rect to the x, y position
    def draw(self, *argv):
        if self.front and argv[0]:
            self.screen.blit(self.front_image, (self.x, self.y))
        else:
            self.screen.blit(self.back_image, (self.x, self.y))

        pygame.display.update()

    # Method to update the visibility of the card
    def update_vis(self, boolean):
        self.front = boolean

    # Method to rotate the card smoothly
    def rotate(self, degrees, is_front):
        is_positive = True if degrees >= 0 else False

        if not is_positive:
            new_degree = degrees * -1
        else:
            new_degree = degrees

        if is_front:
            self.back_image = _rotate_in_place(self.back_image, (self.x, self.y), degrees)
        else:
            self.front_image = _rotate_in_place(self.front_image, (self.x, self.y), degrees)

        while new_degree > 0:
            if is_positive:
                rotated_image, new_rect = _rotate_in_place(
                    self.front_image if is_front else self.back_image, 1)
                self.screen.blit(rotated_image, new_rect.topleft)
            else:
                rotated_image, new_rect = _rotate_in_place(
                    self.front_image if is_front else self.back_image, -1)
                self.screen.blit(rotated_image, new_rect.topleft)

            new_degree -= 1
            if new_degree == 0:
                if is_front:
                    self.front_image = rotated_image
                else:
                    self.back_image = rotated_image

        self.draw(is_front)

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
        pass

    def handle_selected(self, mouse_x, mouse_y):
        return self.rect_card.collidepoint((mouse_x, mouse_y)) and not \
            self.rect_blocked.collidepoint((mouse_x, mouse_y))
