from math import ceil

import pygame

from Cards.Deck.AbstractDeck import AbstractDeck
from Utils.Settings import Settings


def to_int_value(value):
    if value == "3":
        return 3
    if value == "4":
        return 4
    if value == "5":
        return 5
    if value == "6":
        return 6
    if value == "7":
        return 7
    if value == "8":
        return 8
    if value == "9":
        return 9
    if value == "10":
        return 10
    if value == "J":
        return 11
    if value == "Q":
        return 12
    if value == "K":
        return 13
    else:
        return 14


def compare_suits(player, current):
    if (player == "Hearts" and (current == "Diamonds" or current == "Clubs" or current == "Spades")) or \
            (player == "Diamonds" and (current == "Clubs" or current == "Spades")) or \
            (player == "Clubs" and current == "Spades"):
        return True
    else:
        return False


def compare(player, current):
    player_value = player[-1].get_value()
    player_suit = player[-1].get_suit()

    current_value = current[-1].get_value()
    current_suit = current[-1].gets_suit()

    player_value = to_int_value(player_value)
    current_value = to_int_value(current_value)

    if player_value > current_value:
        return True
    if player_value < current_value:
        return False

    return compare_suits(player_suit, current_suit)


class SideDeck(AbstractDeck):
    def __init__(self, x, y, chosen_x, length, collide_point, display, surface):
        super().__init__(display, surface)
        self.x = x
        self.y = y

        self.length = length
        self.collide_point = collide_point

        self.chosen_deck = []

        self.was_chosen_deck = []
        self.to_be_chosen_cards = []

        self.drag_card = []
        self.was_drag_card = []
        self.drag_card_original_index = -1
        self.mouse_x_offset = -1
        self.mouse_y_offset = -1

        self.card_mid_point_y = self.y - self.card_height/2

        self.card_pos = -1

        self.chosen_x = chosen_x
        self.settings = Settings()

        self.background = pygame.Surface((self.card_height, self.length))
        self.half_background = pygame.Surface((self.card_height/2, self.length))
        self.full_card = pygame.Surface((self.card_height, self.card_width))
        self.half_card = pygame.Surface((self.card_height/2, self.length))
        self.half_background.fill(self.settings.bg_color)
        self.full_card.fill(self.settings.bg_color)
        self.half_card.fill(self.settings.bg_color)
        self.background.fill(self.settings.bg_color)

    def draw_deck(self, move_from_shuffle=False, game_update=False, draw=True):
        pass

    def change_pos(self, x, y):
        self.x = x
        self.y = y

    def draw_rest_deck(self, card, for_drag=False):
        index = self.deck.index(card)
        if for_drag:
            for c in range(index, len(self.deck)):
                temp = self.deck[c]
                if not self.was_drag_card.__contains__(temp):
                    self.deck[c].draw(still_drawing=False)
        else:
            for c in range(index + 1 if not for_drag else index, len(self.deck)):
                temp = self.deck[c]
                if ((not (temp.get_chosen() and c == index + 1)) or self.to_be_chosen_cards.__contains__(temp)) \
                        and not self.was_drag_card.__contains__(temp):
                    self.deck[c].draw(still_drawing=False)

    def flip_vis(self, boolean):
        for card in self.deck:
            card.update_vis(boolean)

    def select_deck(self, mouse_x, mouse_y):
        general_deck = self.collide_point.collidepoint((mouse_x, mouse_y))
        collide = False

        for card in self.deck:
            collide = collide or card.handle_selected(mouse_x, mouse_y)

        return collide or general_deck

    def undrag(self, mouse_x, mouse_y):
        i = len(self.deck) - 1
        successful = False
        self.was_drag_card.append(self.drag_card[0])

        self.surface.blit(self.full_card, (self.drag_card[0].cur_pos()))

        while i >= 0:
            card = self.deck[i]
            if card.handle_selected(mouse_x, mouse_y) and not card.equals(self.drag_card[0]):
                self.deck.insert(min(i+1, len(self.deck)), self.drag_card.pop())
                successful = True
                break

            i -= 1

        if not successful:
            self.deck.insert(self.drag_card_original_index, self.drag_card.pop())

        self.draw_deck(game_update=True, draw=False)
        self.update_draw()

        self.drag_card_original_index = -1
        self.mouse_y_offset = -1
        self.mouse_x_offset = -1
        self.drag_card = []

    def move_to_mouse(self, mouse_x, mouse_y):
        new_pos_x = mouse_x + self.mouse_x_offset
        new_pos_y = mouse_y + self.mouse_y_offset

        self.drag_card[0].move(new_pos_x, new_pos_y, drag=True)

    def get_chosen(self):
        return self.chosen_deck.copy()

    def draw_previous(self, index):
        card_pos = self.card_pos
        remaining_width = self.card_width - card_pos
        num_cards = min(index, ceil(remaining_width/card_pos))

        if num_cards == index:
            i = 0
            while i < index:
                card = self.deck[i]
                if not self.was_drag_card.__contains__(card):
                    card.draw(still_drawing=False)
                i += 1
        else:
            i = index - num_cards
            while i < index:
                card = self.deck[i]
                if not self.was_drag_card.__contains__(card):
                    card.draw(still_drawing=False)
                i += 1

    def get_cover_length(self, index, for_chosen):
        card_pos = self.card_pos
        remaining_width = self.card_width - card_pos
        num_cards = min(index, ceil(remaining_width/card_pos))
        min_width = card_pos

        if num_cards == index:
            i = index - 1
            manual_break = False
            while i >= 0:
                card = self.deck[i]
                if for_chosen:
                    if card.get_chosen():
                        min_width = min(self.card_width, min_width + card_pos)
                    else:
                        manual_break = True
                        break
                else:
                    if not card.get_chosen():
                        min_width = min(self.card_width, min_width + card_pos)
                    else:
                        manual_break = True
                        break
                i -= 1
            if not manual_break:
                if not min_width == self.card_width:
                    min_width = self.card_width
        else:
            i = index - 1
            while i >= index - num_cards:
                card = self.deck[i]
                if for_chosen:
                    if card.get_chosen():
                        min_width = min(self.card_width, min_width + card_pos)
                    else:
                        break
                else:
                    if not card.get_chosen():
                        min_width = min(self.card_width, min_width + card_pos)
                    else:
                        break
                i -= 1

        return min_width

    def move_to_chosen(self, card):
        original_length = len(self.chosen_deck)

        if len(self.chosen_deck) == 0:
            self.chosen_deck.append(card)
        else:
            for in_c in self.chosen_deck:
                if not compare(card, in_c):
                    index = self.chosen_deck.index(in_c)
                    self.chosen_deck.insert(index, card)
                    break

        if len(self.chosen_deck) == original_length:
            self.chosen_deck.append(card)

    def move_to_deck(self, card):
        self.chosen_deck.remove(card)

    def handle_selected(self, mouse_x, mouse_y, dragging):
        pass

    def get_pos(self):
        return self.x, self.y

    def reset_chosen(self):
        self.chosen_deck = []

