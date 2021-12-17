import pygame

from Cards.AbstractDeck import AbstractDeck
from Utils.Settings import Settings


class CurrentDeck(AbstractDeck):
    def __init__(self, x, y, width, display, surface):
        super().__init__(display, surface)
        self.x = x
        self.y = y
        self.width = width
        self.settings = Settings()

        self.background = pygame.Surface((self.card_height, self.width))
        self.background.fill(self.settings.bg_color)

    def change_pos(self, x, y):
        self.x = x
        self.y = y

    def draw_deck(self, move_from_shuffle=False):
        if not move_from_shuffle:
            self.display.blit(self.background, (self.x, self.y))

        num_cards = len(self.deck)
        starting = (self.width + self.x) - (num_cards * self.width)
        starting = starting / 2

        for x in self.deck:
            self.display.blit(self.background, (self.x, self.y))

            self.draw_rest_deck(x)
            x.update_vis(True)
            x.move(starting, self.y, False)

            starting += x.get_width()

        self.update()

    def draw_rest_deck(self, card):
        for x in self.deck:
            if x.get_suit != card.get_suit() and x.get_value() != card.get_value():
                x.draw(True)

        self.update()

    def update(self):
        for card in self.deck:
            card.update_draw(True)
