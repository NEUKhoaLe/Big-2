import pygame

from Cards.AbstractDeck import AbstractDeck
from Utils.Settings import Settings


def update_rect(rect, x, y, width, height):
    return rect.update(x, y, width, height)


class PlayerDeck(AbstractDeck):
    def __init__(self, x, y, width, collide_point, display, surface):
        super().__init__(display, surface)
        self.x = x
        self.y = y
        self.width = width
        self.collide_point = collide_point
        self.settings = Settings()

        self.background = pygame.Surface((self.width, self.card_height))
        self.background.fill(self.settings.bg_color)

    def change_pos(self, x, y):
        self.x = x
        self.y = y

    def draw_deck(self, move_from_shuffle=False):
        if not move_from_shuffle:
            self.surface.blit(self.background, (self.x, self.y))

        num_cards = len(self.deck)
        starting = (self.width + self.x) - (num_cards * self.card_width)
        starting = int(starting / 2)

        if num_cards == 0 or num_cards == 1:
            card_pos = self.card_width
        else:
            card_pos = min(self.card_width,
                           round((self.width - self.card_width) / (num_cards - 1)))

        update_rect(self.collide_point, self.x, self.y,
                    (num_cards * self.card_width), self.card_height)

        for x in self.deck:
            if not x.get_chosen():
                self.surface.blit(self.background, (self.x, self.y))

                self.draw_rest_deck(x)

                x.update_vis(True)
                x.move(starting, self.y, False)
                x.update_card_block_area(starting + card_pos, self.card_height,
                                         self.card_width - card_pos, self.card_height)

            # Do this portion
            else:
                pass

            self.update()
            starting += card_pos

    def draw_rest_deck(self, card):
        for x in self.deck:
            if x.get_suit != card.get_suit() and x.get_value() != card.get_value():
                x.draw(still_drawing=False)

        # self.update()

    def update(self):
        for card in self.deck:
            card.update_draw(True)

        pygame.display.flip()

    def flip_vis(self, boolean):
        for card in self.deck:
            card.update_vis(boolean)
