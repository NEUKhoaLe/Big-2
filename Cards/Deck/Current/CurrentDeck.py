import pygame

from Cards.Deck.AbstractDeck import AbstractDeck
from Utils.Settings import Settings


def update_rect(rect, x, y, width, height):
    return rect.update(x, y, width, height)


class CurrentDeck(AbstractDeck):
    def __init__(self, x, y, width, display, surface):
        super().__init__(display, surface)
        self.x = x
        self.y = y
        self.width = width
        self.settings = Settings()
        self.card_pos = -1

        self.full_card = pygame.Surface((self.card_width, self.card_height))
        self.full_card.fill(self.settings.bg_color)

        self.background = pygame.Surface((self.width, self.card_height))
        self.background.fill(self.settings.bg_color)

    def change_pos(self, x, y):
        self.x = x
        self.y = y

    def draw_deck(self, move_from_shuffle=False, game_update=False, draw=True):
        if not move_from_shuffle:
            self.surface.blit(self.background, (self.x, self.y))

        num_cards = len(self.deck)
        starting = max(((self.width + self.x) - (num_cards * self.card_width)) / 2, self.x)

        if num_cards == 0 or num_cards == 1:
            self.card_pos = self.card_width
        else:
            self.card_pos = min(self.card_width,
                                round((self.width - self.card_width) / (num_cards - 1)))

        for i in range(len(self.deck)):
            self.surface.blit(self.full_card, (starting + self.card_pos, self.y))

            x = self.deck[i]

            # We draw the background, then draw the previous cards, then proceed.
            if draw:
                # self.draw_previous(i)
                self.draw_rest_deck(x)
                pass

            x.update_vis(True)
            x.move(starting, self.y, shuffle=True, draw=draw)

            if i != len(self.deck) - 1:
                if not self.deck[i + 1].get_chosen():
                    x.update_card_block_area(starting + self.card_pos, self.y,
                                             self.card_width - self.card_pos, self.card_height)
                else:
                    x.update_card_block_area(starting + self.card_pos, self.y,
                                             self.card_width - self.card_pos, self.card_height/2)
            else:
                x.update_card_block_area(starting + self.card_pos, self.y, 0, 0)

            # Do this portion
            starting += self.card_pos

        # self.update(game_update)

    def draw_rest_deck(self, card):
        index = self.deck.index(card)
        for c in range(index + 1, len(self.deck)):
            self.deck[c].draw(still_drawing=False)

    def update(self, game_update):
        for card in self.deck:
            card.update_draw(True)

        if not game_update:
            pygame.display.flip()

    def get_pos(self):
        return self.x, self.y
