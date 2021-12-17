from Cards.Cards import Cards


class AbstractDeck:
    def __init__(self, display, surface, deck=None):
        if deck is None:
            self.deck = []
        else:
            self.deck = deck

        self.display = display
        self.surface = surface
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
            return self.deck.remove(len(self.deck) - 1)
        elif cards == "first":
            return self.deck.remove(0)
        elif isinstance(cards, int):
            return self.deck.pop(cards)
        elif isinstance(cards, Cards):
            return self.deck.remove(cards)

    def transfer_all_cards_to_deck(self, deck):
        deck.add_card(self.deck)
        self.deck = []

    def get_length(self):
        return len(self.deck)

    def move_to_chosen(self):
        pass

    def card_change_in_play(self, index, boolean):
        pass

    def draw_deck(self, move_from_shuffle):
        pass

    def change_pos(self, x, y):
        pass

    def update(self):
        pass

    def reset(self):
        pass

    def flip_vis(self, boolean):
        pass

    """
    A deck needs a:
    - list to store the cards
    - Method to add cards
    - Method to remove cards
    - To draw selective cards
    - Reset method.
    """