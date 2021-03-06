import pygame

from Cards.Cards import Cards
from Cards.ServerCard import ServerCard


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
            return self.deck.pop(len(self.deck) - 1)
        elif cards == "first":
            return self.deck.pop(0)
        elif isinstance(cards, int):
            return self.deck.pop(cards)
        elif isinstance(cards, Cards):
            return self.deck.remove(cards)

    def transfer_all_cards_to_deck(self, deck):
        temp_deck = []

        if len(deck) != 0 and type(deck[0]) is ServerCard:
            for card in deck:
                if not self.contains(card):
                    temp = Cards(self.display, self.surface, card.value, card.suit, card.front_image, card.back_image)
                    temp.x = card.x
                    temp.y = card.y
                    temp.chosen = card.chosen
                    temp.in_play = card.in_play
                    temp.rect_card = card.rect_card
                    temp.rect_blocked = card.rect_blocked
                    temp.orientation = card.orientation
                    temp.width = card.width
                    temp.height = card.height

                    temp_deck.append(temp)
        else:
            for card in deck:
                temp_deck.append(card)

        self.deck = temp_deck

    def contains(self, card):
        for c in self.deck:
            if c.equals(card):
                return True

        return False

    def get_length(self):
        return len(self.deck)

    def handle_selected(self, mouse_x, mouse_y, dragging):
        pass

    def move_to_deck(self, card):
        pass

    def card_change_in_play(self, index, boolean):
        pass

    def draw_deck(self, move_from_shuffle, game_update=False, draw=True):
        pass

    def update_draw(self):
        for card in self.deck:
            card.draw(still_drawing=False)

        self.update(False)

    def change_pos(self, x, y):
        pass

    def get_pos(self):
        pass

    def update(self, game_update):
        for card in self.deck:
            card.update_draw(True)

        if not game_update:
            pygame.display.flip()

    def reset(self):
        pass

    def shuffle_deck(self):
        pass

    def get_deck(self):
        return self.deck.copy()
