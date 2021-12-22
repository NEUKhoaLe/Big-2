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
        self.chosen_y = chosen_y

        self.collide_point = collide_point
        self.settings = Settings()

        self.background = pygame.Surface((self.width, self.card_height))
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
                    (num_cards * self.card_width), self.card_height)

        for x in self.deck:
            self.surface.blit(self.background, (starting + 100, self.y))
            self.draw_rest_deck(x)

            if x.cur_pos() == (self.settings.shuffle_x, self.settings.shuffle_y):
                x.rotate(180)

            if not x.get_chosen():
                x.update_vis(True)
                if x.cur_pos()[1] == self.y:
                    x.move(starting, self.y, False)
                else:
                    x.move(starting, self.y, False)

                x.move(starting, self.y, False)
                x.update_card_block_area(starting + card_pos, self.y,
                                         self.card_width - card_pos, self.card_height)

            # Do this portion
            else:
                x.move(starting, self.chosen_y, False)
                original_x, original_y = x.cur_pos()
                x.update_card_block_area(original_x + card_pos,
                                         self.y,
                                         self.card_width - card_pos,
                                         self.y - self.chosen_y)

            starting += card_pos

            if not game_update and x.cur_pos()[1] != self.y:
                self.update()

    def draw_rest_deck(self, card):
        index = self.deck.index(card)
        for c in range(index + 1, len(self.deck)):
            self.deck[c].draw(still_drawing=False)

    def update(self):
        for card in self.deck:
            card.update_draw(True)

        pygame.display.flip()

    def flip_vis(self, boolean):
        for card in self.deck:
            card.update_vis(boolean)

    def select_deck(self, mouse_x, mouse_y):
        return self.collide_point.collidepoint((mouse_x, mouse_y))

    def get_pos(self):
        return self.x, self.y

    def handle_selected(self, mouse_x, mouse_y):
        for card in self.deck:
            if card.handle_selected(mouse_x, mouse_y):
                if card.get_chosen():
                    self.move_to_deck(card)
                    card.change_chosen(False)
                    return
                else:
                    self.move_to_chosen(card)
                    card.change_chosen(True)
                    return

    def move_to_deck(self, card):
        self.chosen_deck.remove(card)

    def move_to_chosen(self, card):
        self.chosen_deck.append(card)
