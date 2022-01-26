from Cards.Deck.AbstractDeck import AbstractDeck
from Cards.ServerCard import ServerCard
from Utils.ServerSettings import ServerSettings


class ServerShuffleDeck:
    def __init__(self, x, y, deck=None):
        if deck is None:
            self.deck = []
        else:
            self.deck = deck

        self.x = x
        self.y = y

        self.settings = ServerSettings()

        self.card_width = 100
        self.card_height = 150

    def add_card(self, cards):
        if isinstance(cards, list):
            for card in cards:
                self.deck.append(card)
        else:
            self.deck.append(cards)

    def remove_card(self, cards):
        if isinstance(cards, list):
            for card in cards:
                self.deck.remove(card)
        elif cards == "last":
            return self.deck.pop(len(self.deck) - 1)
        elif cards == "first":
            return self.deck.pop(0)
        elif isinstance(cards, int):
            return self.deck.pop(cards)
        elif isinstance(cards, ServerCard):
            return self.deck.remove(cards)

    def transfer_all_cards_to_deck(self, deck):
        self.deck = deck.copy()

    def get_length(self):
        return len(self.deck)

    def get_deck(self):
        return self.deck.copy()

    def move_deck(self):
        for x in self.deck:
            x.update_vis(False)
            x.move(self.x, self.y)

    def change_pos(self, x, y, to_shuffle=False):
        if to_shuffle:
            self.x = 450
            self.y = 425
        else:
            self.x = x
            self.y = y

    def card_change_in_play(self, index, boolean):
        self.deck[index].change_in_play(boolean)

    def get_pos(self):
        return self.x, self.y
