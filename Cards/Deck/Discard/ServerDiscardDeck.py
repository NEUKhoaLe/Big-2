from Cards.ServerCard import ServerCard
from Utils.ServerSettings import ServerSettings


class ServerDiscardDeck:
    def __init__(self, x, y):
        self.deck = []

        self.card_width = 100
        self.card_height = 150

        self.x = x
        self.y = y
        self.settings = ServerSettings()

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

    def change_pos(self, x, y):
        self.x = x
        self.y = y

    def _deck(self):
        for x in self.deck:
            x.move(self.x, self.y)
            x.update_vis(False)

    def get_pos(self):
        return self.x, self.y
