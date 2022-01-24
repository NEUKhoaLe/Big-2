from math import ceil

import pygame

from Cards.Deck.AbstractDeck import AbstractDeck
from Utils.Settings import Settings


class TopBottomDeck(AbstractDeck):
    def __init__(self, x, y, chosen_y, width, collide_point, display, surface):
        super().__init__(display, surface)
        self.x = x
        self.y = y

        self.width = width
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

        self.chosen_y = chosen_y
        self.settings = Settings()

        self.background = pygame.Surface((self.width, self.card_height))
        self.half_background = pygame.Surface((self.width, self.card_height/2))
        self.full_card = pygame.Surface((self.card_width, self.card_height))
        self.half_card = pygame.Surface((self.width, self.card_height/2))
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

    def get_cover_width(self, index, for_chosen):
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
        self.chosen_deck.append(card)

    def move_to_deck(self, card):
        self.chosen_deck.remove(card)

    def handle_selected(self, mouse_x, mouse_y, dragging):
        pass

    def get_pos(self):
        return self.x, self.y
