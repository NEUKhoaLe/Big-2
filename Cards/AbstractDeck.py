import pygame


class AbstractDeck:
    def __init__(self, display, surface):
        self.__init__([], display, surface)
        self.card_width = 100
        self.card_height = 150

    def __init__(self, deck, display, surface):
        self.deck = deck
        self.display = display
        self.surface = surface

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
        else:
            self.deck.remove(cards)

    def draw_deck(self, move_from_shuffle):
        pass

    def change_pos(self, x, y):
        pass

    def update(self):
        pass

    def reset(self):
        pass

    """
    A deck needs a:
    - list to store the cards
    - Method to add cards
    - Method to remove cards
    - To draw selective cards
    - Reset method.
    """