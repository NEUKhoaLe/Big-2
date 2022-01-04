import pygame.display

from Cards.AbstractDeck import AbstractDeck
from Utils.Settings import Settings


class DiscardDeck(AbstractDeck):
    def __init__(self, x, y, display, surface):
        super().__init__(display, surface)

        self.x = x
        self.y = y
        self.settings = Settings()

    def change_pos(self, x, y):
        self.x = x
        self.y = y

    def draw_deck(self, move_from_shuffle=False, game_update=False):
        if len(self.deck) != 0:
            card = self.deck[len(self.deck) - 1]
            card.draw(is_front=False)

            self.update(game_update)

        else:
            for x in self.deck:
                x.move(self.x, self.y, False)
                x.update_vis(False)

                if not game_update:
                    self.update(game_update)

    def update(self, game_update):
        for card in self.deck:
            card.update_draw(True)

        if not game_update:
            pygame.display.flip()

    def get_pos(self):
        return self.x, self.y

