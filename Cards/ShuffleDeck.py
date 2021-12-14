from Cards.AbstractDeck import AbstractDeck
from Utils.Settings import Settings


class ShuffleDeck(AbstractDeck):
    def __init__(self, x, y, display, surface):
        super().__init__(display, surface)
        self.x = x
        self.y = y
        self.settings = Settings()

    def change_pos(self, x, y):
        self.x = x
        self.y = y

    def draw_deck(self, move_from_shuffle=False):
        for x in self.deck:
            x.update_vis(False)
            x.move(self.x, self.y, True)

        self.update()

    def update(self):
        for card in self.deck:
            card.update_draw(True)