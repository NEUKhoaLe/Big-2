import pygame.display

from Cards.Deck.AbstractDeck import AbstractDeck
from Utils.Settings import Settings


class DiscardDeck(AbstractDeck):
    def __init__(self, x, y, display, surface):
        super().__init__(display, surface)

        self.x = x
        self.y = y
        self.discard_x_size = 60
        self.discard_y_size = 100
        self.settings = Settings()

    def change_pos(self, x, y):
        self.x = x
        self.y = y

    def draw_deck(self, move_from_shuffle=False, game_update=False, draw=True):
        if len(self.deck) != 0:
            for x in self.deck:
                x.scale(self.discard_x_size, self.discard_y_size)
                x.move(self.x, self.y, True)
                x.update_vis(False)

            card = self.deck[len(self.deck) - 1]
            card.draw(is_front=False)

            # self.update(game_update)

    def update(self, game_update):
        for card in self.deck:
            card.update_draw(True)

        if not game_update:
            pygame.display.flip()

    def get_pos(self):
        return self.x, self.y
