import pygame

from Utils.ServerSettings import ServerSettings


def _rotate_in_place(image, top_left, degree):
    rotated_image = pygame.transform.rotate(image, degree)
    rotated_rect = rotated_image.get_rect(center=image.get_rect(topleft=top_left).center)
    return rotated_image, rotated_rect


class ServerCard:

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        self.settings = ServerSettings()

        self.width = 100
        self.height = 150

        # Keep track of orientation
        self.orientation = "vertical"

        self.front = True

        self.x = -200
        self.y = -200

        self.chosen = False

        self.in_play = False

        self.rect_card = pygame.Rect(self.x, self.y, self.width, self.height)
        self.rect_blocked = pygame.Rect(0, 0, 0, 0)

    def move(self, x, y):
        self.x = x
        self.y = y

        self.update_card_collision(self.x, self.y)

    def update_vis(self, boolean):
        self.front = boolean

    def rotate(self, degrees):
        if degrees == 90 or degrees == 270:
            if self.orientation == "vertical":
                self.rect_card = pygame.Rect(self.x, self.y, self.height, self.width)
                self.orientation = "horizontal"
                return
            elif self.orientation == "horizontal":
                self.rect_card = pygame.Rect(self.x, self.y, self.width, self.height)
                self.orientation = "vertical"
                return

        self.update_card_collision(self.x, self.y)

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def cur_pos(self):
        return self.x, self.y

    def change_chosen(self, boolean):
        self.chosen = boolean

    def get_chosen(self):
        return self.chosen

    # Change the status of the in play instanceself.rect_card = self.front_image.get_rect()
    def change_in_play(self, boolean):
        self.in_play = boolean

    # return the status of the in play instance
    def get_in_play(self):
        return self.in_play

    def update_card_collision(self, x, y):
        self.rect_card.move_ip(x, y)

    def update_card_block_area(self, x, y, width, height):
        self.rect_blocked.update(x, y, width, height)

    def handle_selected(self, mouse_x, mouse_y):
        return self.rect_card.collidepoint((mouse_x, mouse_y)) and not \
            self.rect_blocked.collidepoint((mouse_x, mouse_y))

    def get_suit(self):
        return self.suit

    def get_value(self):
        return self.value

    def equals(self, card):
        return (self.get_value() == card.get_value()) and (self.get_suit() == card.get_suit())
