from Cards.ServerCard import ServerCard
from Utils.ServerSettings import ServerSettings


class ServerCurrentDeck:
    def __init__(self, x, y, width):
        self.deck = []
        self.card_width = 100
        self.card_height = 150

        self.x = x
        self.y = y
        self.width = width
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

    def move_deck(self):
        num_cards = len(self.deck)
        starting = (self.width + self.x) - (num_cards * self.width)
        starting = starting / 2

        for x in self.deck:
            x.update_vis(True)
            x.move(starting, self.y)

            starting += x.get_width()

    def get_pos(self):
        return self.x, self.y
