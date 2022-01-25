import pygame

from Board.AbstractBoard import AbstractBoard
from Cards.Deck.CurrentDeck import CurrentDeck
from Cards.Deck.DiscardDeck import DiscardDeck
from Cards.Deck.PlayDeck.PlayerDeck import PlayerDeck
from Cards.Deck.PlayDeck.OppositeDeck import OppositeDeck


def is_same(operating_deck):
    i = 0

    while i < len(operating_deck) - 1:
        if operating_deck[i].get_value() != operating_deck[i+1].get_value():
            return False

    return True


class Board2(AbstractBoard):
    def __init__(self, display, surface):
        super().__init__(display, surface)

        self.opposite_deck_collide_point = pygame.Rect(self.settings.opposite_deck_2_x, self.settings.opposite_y,
                                                       0, 0)
        self.player_deck_collide_point = pygame.Rect(self.settings.player_deck_2_x, self.settings.player_y,
                                                     0, 0)

        # The layout of the board
        # The player's Deck
        self.player_deck = PlayerDeck(self.settings.player_deck_2_x, self.settings.player_y,
                                      self.settings.player_chosen_y, self.settings.play_deck_width_2,
                                      self.player_deck_collide_point, self.display, self.surface)
        # The opponent's Deck
        self.opposite_deck = OppositeDeck(self.settings.opposite_deck_2_x, self.settings.opposite_y,
                                          self.settings.opposite_chosen_y, self.settings.play_deck_width_2,
                                          self.opposite_deck_collide_point, self.display, self.surface)

        # The current play deck: where we will place the cards
        # That are currently being played.
        self.current_deck = CurrentDeck(self.settings.current_deck_2_x, self.settings.current_deck_y,
                                        self.settings.play_deck_width_2, self.display, self.surface)
        # The Discard pile
        self.discard_deck = DiscardDeck(self.settings.discard_deck_x_2, self.settings.discard_deck_y_2,
                                        self.display, self.surface)

    # Method to draw a given deck given a deck type
    # If it is a shuffle deck: we will draw only the top back
    # of the card
    # If it is the opponent's deck, then we will draw each card
    # moving to its place, reversed 180 degrees
    # If it is discard, we also only draw the top of the deck
    # card back
    # If it is the current play pile, we draw the card front
    # If it is in the chosen pile, we draw the card moving up
    # half its length
    def draw_deck(self, deck_type, game_update):
        if deck_type == "shuffle":
            self.move_to_shuffle_pos(game_update)
        elif deck_type == "opposite":
            if game_update:
                self.opposite_deck.update_draw()
            else:
                self.opposite_deck.draw_deck(False, game_update)
        elif deck_type == "current":
            if game_update:
                self.current_deck.update_draw()
            else:
                self.current_deck.draw_deck(False, game_update)
        elif deck_type == "discard":
            if game_update:
                self.discard_deck.update_draw()
            else:
                self.discard_deck.draw_deck(False, game_update)
        elif deck_type == "player":
            if game_update:
                self.player_deck.update_draw()
            else:
                self.player_deck.draw_deck(False, game_update)

    # Method to deal the shuffled card.
    # takes in the winner of the last game.
    # deals in counter clock-wise
    # Must implement the move.
    def deal(self, last_winner):
        counter = 0
        if last_winner == "player":
            i = self.shuffledeck.get_length() - 1
            while i >= 0:
                self.shuffledeck.card_change_in_play(i, True)
                if counter % 2 == 0:
                    self.player_deck.add_card(self.shuffledeck.remove_card("last"))
                    self.player_deck.draw_deck(True)
                else:
                    self.opposite_deck.add_card(self.shuffledeck.remove_card("last"))
                    self.opposite_deck.draw_deck(True)
                counter += 1
                i -= 1
        else:
            i = self.shuffledeck.get_length() - 1
            while i >= 0:
                self.shuffledeck.card_change_in_play(i, True)
                if counter % 2 == 1:
                    self.opposite_deck.add_card(self.shuffledeck.remove_card("last"))
                    self.opposite_deck.draw_deck(True)
                else:
                    self.player_deck.add_card(self.shuffledeck.remove_card("last"))
                    self.player_deck.draw_deck(True)
                counter += 1
                i -= 1

        pygame.display.flip()

    # Method to move card from play pile to chosen pile
    def move_play_to_chosen(self, card, deck_type):
        pass

    def move_chosen_to_play(self, card, deck_type):
        pass

    # Method to move card from pile to the play pile
    def move_chosen_to_current(self, pile_from, cards):
        if pile_from == "player":
            pass
        elif pile_from == "opposite":
            pass

    # Method to flip the visibility.
    def flip_vis(self, deck_type, boolean):
        if deck_type == "opposite":
            self.opposite_deck.flip_vis(boolean)
        elif deck_type == "player":
            self.player_deck.flip_vis(boolean)

    def select_deck(self, mouse_x, mouse_y):
        if self.player_deck.select_deck(mouse_x, mouse_y):
            return "player"
        elif self.opposite_deck.select_deck(mouse_x, mouse_y):
            return "opposite"

    # Handle collision. Choosing a card. Passes in x and y position of mouse. First find which deck was chosen
    # and then go through every card in that deck to find the card. Move that card to the chosen
    # If a chosen card is selected, then it is "unchosen" i.e. removed from the chosen pile
    def choose_card(self, mouse_x, mouse_y, cur_player, dragging):
        if self.select_deck(mouse_x, mouse_y) == "player" and cur_player == "player":
            return self.player_deck.handle_selected(mouse_x, mouse_y, dragging)
        elif self.select_deck(mouse_x, mouse_y) == "opposite" and cur_player == "opposite":
            return self.opposite_deck.handle_selected(mouse_x, mouse_y, dragging)
        else:
            return "Not Selected " + cur_player

    def rotate_deck(self, order):
        temp_deck = self.opposite_deck.get_deck()
        self.opposite_deck.transfer_all_cards_to_deck(self.player_deck.get_deck())
        self.player_deck.transfer_all_cards_to_deck(temp_deck)

    def move_to_discard(self):
        pass

    def play(self, turn):
        operating_deck = None
        if turn == "player":
            operating_deck = self.player_deck.get_chosen()
        elif turn == "opposite":
            operating_deck = self.opposite_deck.get_chosen()

        if self.valid_move(operating_deck):
            pass

    # It is a valid move if:
    # - There is cards in the chosen deck
    # - there is no cards in the current pile
    # - there are the same number of cards in the chosen and the current deck
    # - If there are more than 1 card, then the cards must either be:
    # - Doubles, Triples, or Quadruples
    # - Consecutive, with at least 3 in a row
    # - Doubles consecutive, with at least 3
    # - If there are only one card, then it must follow these rules:
    # - Specials > 2 > A > K > Q > J > 10 > 9 > 8 > 7 > 6 > 5 > 4 > 3 > 2
    # - Hearts > Diamonds > Clubs > Spades
    # - Specials have to be these:
    # - Doubles Consecutive, with 3 in a row being better than ONE 2 of any suit
    # - Doubles Consecutive with 4 in a row or better is stronger than TWO 2 of any suits,
    # - And can be played at any point.
    # - Quadruple of any number is stronger than TWO 2 of any suits
    # Special Rules:
    # - If a player has 12 cards that is in a row (3 to A) they automatically win
    # - If a player has 6 pairs of cards, then they automatically win
    # - If a player has 4 2's, they automatically win
    def valid_move(self, operating_deck):
        if len(operating_deck) == 0:
            return False

        if len(operating_deck) != self.current_deck.get_length():
            return False

        if self.current_deck.get_length() == 0:
            if len(operating_deck) == 1:
                return True
            elif len(operating_deck) == 2:
                return is_same(operating_deck)
            elif len(operating_deck) >= 3:
                valid = False
                valid = valid or self.is_consecutive(operating_deck)
                if len(operating_deck) == 3:
                    valid = valid or is_same(operating_deck)
                if len(operating_deck) == 4:
                    valid = valid or is_same(operating_deck)
                if len(operating_deck) % 2 == 0 and len(operating_deck) >= 6:
                    valid = valid or self.is_double_consecutive(operating_deck)

    def is_consecutive(self, operating_deck):
        i = 1
        while i < len(operating_deck):
            if operating_deck[i-1].get_value() != operating_deck[i].get_value() + 1:
                return False

        return True

    def is_double_consecutive(self, operating_deck):
        interval = len(operating_deck) / 2
        i = 0
        temp = []
        valid = True

        while i < interval:
            temp.append(operating_deck[i * 2])
            valid = valid and is_same([operating_deck[i * 2], operating_deck[(i * 2) + 1]])
            i += 1

        return valid and self.is_consecutive(temp)

    def move_to_mouse(self, mouse_x, mouse_y, turn):
        if turn == "player":
            self.player_deck.move_to_mouse(mouse_x, mouse_y)
        elif turn == "opposite":
            self.opposite_deck.move_to_mouse(mouse_x, mouse_y)

    def undrag(self, mouse_x, mouse_y, turn):
        if turn == "player":
            self.player_deck.undrag(mouse_x, mouse_y)
        elif turn == "opposite":
            self.opposite_deck.undrag(mouse_x, mouse_y)
