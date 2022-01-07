from math import ceil

import pygame

from Cards.AbstractDeck import AbstractDeck
from Utils.Settings import Settings


def update_rect(rect, x, y, width, height):
    return rect.update(x, y, width, height)


class OpponentDeck(AbstractDeck):
    def __init__(self, x, y, chosen_y, width, collide_point, display, surface):
        super().__init__(display, surface)
        self.x = x
        self.y = y
        self.width = width

        self.chosen_deck = []
        self.was_chosen_deck = []
        self.to_be_chosen_cards = []
        self.chosen_y = chosen_y

        self.collide_point = collide_point
        self.settings = Settings()

        self.background = pygame.Surface((self.width, self.card_height))
        self.half_card = pygame.Surface((self.width, self.card_height/2))
        self.half_card.fill(self.settings.bg_color)
        self.background.fill(self.settings.bg_color)

    def change_pos(self, x, y):
        self.x = x
        self.y = y

    def draw_deck(self, move_from_shuffle=False, game_update=False):
        if not move_from_shuffle:
            self.surface.blit(self.background, (self.x, self.y))

        num_cards = len(self.deck)
        starting = max((self.width + self.x) - (num_cards * self.card_width), self.x)

        if num_cards == 0 or num_cards == 1:
            card_pos = self.card_width
        else:
            card_pos = min(self.card_width,
                           round((self.width - self.card_width) / (num_cards - 1)))

        update_rect(self.collide_point, self.x, self.y,
                    min((num_cards * self.card_width), self.width), self.card_height)

        for i in range(len(self.deck)):
            self.surface.blit(self.background, (starting + 100, self.y))

            x = self.deck[i]

            if x.cur_pos() == (self.settings.shuffle_x, self.settings.shuffle_y):
                x.rotate(180)

            if not x.get_chosen():
                # We draw the background, then draw the previous cards, then proceed.
                if self.was_chosen_deck.__contains__(x):
                    width = self.get_cover_width(i, card_pos, for_chosen=False)
                    self.half_card = pygame.Surface((width + 2, self.card_height/2))
                    self.half_card.fill(self.settings.bg_color)
                    self.surface.blit(self.half_card,
                                      (starting + self.card_width - width, self.y + self.card_height))
                    self.was_chosen_deck.remove(x)

                self.draw_previous(i, card_pos)

                self.draw_rest_deck(x)

                x.update_vis(True)
                if x.cur_pos()[1] == self.y or x.cur_pos()[1] == self.chosen_y:

                    x.move(starting, self.y, True)
                else:
                    x.move(starting, self.y, False)

                if i != len(self.deck) - 1:
                    if not self.deck[i+1].get_chosen():
                        x.update_card_block_area(starting + card_pos, self.y,
                                                 self.card_width - card_pos, self.card_height)
                    else:
                        x.update_card_block_area(starting + card_pos, self.y + self.card_height/2,
                                                 self.card_width - card_pos, self.card_height/2)
                else:
                    x.update_card_block_area(starting + card_pos, self.y, 0, 0)

            # Do this portion
            else:
                if self.to_be_chosen_cards.__contains__(x):
                    width = self.get_cover_width(i, card_pos, for_chosen=True)
                    self.half_card = pygame.Surface((width, self.card_height/2 + 2))
                    self.half_card.fill(self.settings.bg_color)
                    self.surface.blit(self.half_card,
                                      (starting + self.card_width - width, self.y))
                    self.to_be_chosen_cards.remove(x)

                self.draw_previous(i, card_pos)

                self.draw_rest_deck(x)

                x.move(starting, self.chosen_y, False)
                original_x, original_y = x.cur_pos()

                if i != len(self.deck) - 1:
                    if not self.deck[i+1].get_chosen():
                        x.update_card_block_area(original_x + card_pos,
                                                 self.y + self.card_height/2,
                                                 self.card_width - card_pos,
                                                 self.chosen_y - self.y)
                    else:
                        x.update_card_block_area(original_x + card_pos,
                                                 self.chosen_y,
                                                 self.card_width - card_pos,
                                                 self.card_height)

                else:
                    x.update_card_block_area(original_x + card_pos, self.y, 0, 0)

            starting += card_pos

            self.update(game_update)

    def draw_rest_deck(self, card):
        index = self.deck.index(card)
        for c in range(index + 1, len(self.deck)):
            if (not (self.deck[c].get_chosen() and c == index + 1)) \
                    or self.to_be_chosen_cards.__contains__(self.deck[c]):
                self.deck[c].draw(still_drawing=False)

    def update(self, game_update):
        for card in self.deck:
            card.update_draw(True)

        if not game_update:
            pygame.display.flip()

    def flip_vis(self, boolean):
        for card in self.deck:
            card.update_vis(boolean)

    def select_deck(self, mouse_x, mouse_y):
        general_deck = self.collide_point.collidepoint((mouse_x, mouse_y))
        collide = False

        for card in self.deck:
            collide = collide or card.handle_selected(mouse_x, mouse_y)

        return collide or general_deck

    def get_pos(self):
        return self.x, self.y

    def handle_selected(self, mouse_x, mouse_y):
        i = len(self.deck) - 1
        while i >= 0:
            card = self.deck[i]
            if card.handle_selected(mouse_x, mouse_y):
                if card.get_chosen():
                    self.move_to_deck(card)
                    card.change_chosen(False)
                    self.was_chosen_deck.append(card)
                    return
                else:
                    self.move_to_chosen(card)
                    card.change_chosen(True)
                    self.to_be_chosen_cards.append(card)
                    return
            i -= 1

    def move_to_deck(self, card):
        self.chosen_deck.remove(card)

    def move_to_chosen(self, card):
        self.chosen_deck.append(card)

    def get_cover_width(self, index, card_pos, for_chosen):
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

    def draw_previous(self, index, card_pos):
        remaining_width = self.card_width - card_pos
        num_cards = min(index, ceil(remaining_width/card_pos))

        if num_cards == index:
            i = 0
            while i < index:
                card = self.deck[i]
                card.draw(still_drawing=False)
                i += 1
        else:
            i = index - num_cards
            while i < index:
                card = self.deck[i]
                card.draw(still_drawing=False)
                i += 1
