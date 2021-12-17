from Cards.AbstractDeck import AbstractDeck
from Utils.Settings import Settings


class ShuffleDeck(AbstractDeck):
    def __init__(self, x, y, display, surface, deck=None):
        if deck is None:
            super().__init__(display, surface)
        else:
            super().__init__(display, surface, deck)
        self.x = x
        self.y = y
        self.settings = Settings()

    def change_pos(self, x, y, to_shuffle=False):
        if to_shuffle:
            self.x = 450
            self.y = 425
        else:
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

    def shuffle(self):
        pass

    def card_change_in_play(self, index, boolean):
        self.deck[index].change_in_play(boolean)