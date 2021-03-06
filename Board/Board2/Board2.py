from random import Random

import pygame

from Board.AbstractBoard import AbstractBoard
from Cards.Deck.Current.CurrentDeck import CurrentDeck
from Cards.Deck.Discard.DiscardDeck import DiscardDeck
from Cards.Deck.PlayDeck.Player.PlayerDeck import PlayerDeck
from Cards.Deck.PlayDeck.Opposite.OppositeDeck import OppositeDeck


def is_same(operating_deck):
    i = 0

    while i < len(operating_deck) - 1:
        if operating_deck[i].get_value() != operating_deck[i + 1].get_value():
            return False

        i += 1

    return True


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
    elif value == "A":
        return 14
    else:
        return 15


def compare_suits(player, current):
    if (player == "Hearts" and (current == "Diamonds" or current == "Clubs" or current == "Spades")) or \
            (player == "Diamonds" and (current == "Clubs" or current == "Spades")) or \
            (player == "Clubs" and current == "Spades"):
        return "player"
    else:
        return "current"


def compare(player, current):
    player_value = player.get_value()
    player_suit = player.get_suit()

    current_value = current.get_value()
    current_suit = current.get_suit()

    player_value = to_int_value(player_value)
    current_value = to_int_value(current_value)

    if player_value > current_value:
        return "player"
    if player_value < current_value:
        return "current"

    return compare_suits(player_suit, current_suit)


class Board2(AbstractBoard):
    def __init__(self, display, surface, player_id=-1):
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

        self.player_id = player_id

        self.board_dict = {}
        if player_id == 1 or player_id == -1:
            self.board_dict[1] = self.player_deck
            self.board_dict[2] = self.opposite_deck
        elif player_id == 2:
            self.board_dict[2] = self.player_deck
            self.board_dict[1] = self.opposite_deck

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
        if last_winner == "player":
            counter = 1
            i = self.shuffledeck.get_length() - 1
            while i >= 0:
                self.shuffledeck.card_change_in_play(i, True)
                self.board_dict[counter % 2 + 1].add_card(self.shuffledeck.remove_card("last"))
                self.board_dict[counter % 2 + 1].draw_deck(True)
                counter += 1
                i -= 1

                pygame.display.flip()
        else:
            i = self.shuffledeck.get_length() - 1
            counter = 1
            while i >= 0:
                self.shuffledeck.card_change_in_play(i, True)
                self.board_dict[counter % 2 + 1].add_card(self.shuffledeck.remove_card("last"))
                self.board_dict[counter % 2 + 1].draw_deck(True)
                counter += 1
                i -= 1

                pygame.display.flip()

    # Method to move card from pile to the play pile
    def move_chosen_to_current(self, pile_from):
        if pile_from == "player":
            player_chosen = self.player_deck.get_chosen()
            self.current_deck.transfer_all_cards_to_deck(player_chosen)
            self.player_deck.remove_card(player_chosen)
            self.player_deck.reset_chosen()
        elif pile_from == "opposite":
            opposite_chosen = self.opposite_deck.get_chosen()
            self.current_deck.transfer_all_cards_to_deck(opposite_chosen)
            self.opposite_deck.remove_card(opposite_chosen)
            self.opposite_deck.reset_chosen()

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
        if self.select_deck(mouse_x, mouse_y) == "player":
            return self.player_deck.handle_selected(mouse_x, mouse_y, dragging)
        if self.select_deck(mouse_x, mouse_y) == "opposite":
            return self.opposite_deck.handle_selected(mouse_x, mouse_y, dragging)

    def rotate_deck(self, order):
        if order == [2, 1]:
            temp_deck = self.opposite_deck.get_deck()
            self.opposite_deck.transfer_all_cards_to_deck(self.player_deck.get_deck())
            self.player_deck.transfer_all_cards_to_deck(temp_deck)

    def move_to_discard(self):
        current_deck = self.current_deck.get_deck()
        self.discard_deck.transfer_all_cards_to_deck(current_deck)
        self.current_deck.remove_card(current_deck)

    def check_winner(self):
        player = self.player_deck.get_deck()
        opposite = self.opposite_deck.get_deck()

        if len(player) == 0:
            return "player"

        if len(opposite) == 0:
            return "opposite"

        player_2_count = 0
        for card in player:
            if card.get_value() == "2":
                player_2_count += 1

        if player_2_count == 4:
            return "player"

        opposite_2_count = 0
        for card in opposite:
            if card.get_value() == "2":
                opposite_2_count += 1

        if opposite_2_count == 4:
            return "opposite"

        return "none"

    def play(self, player, turn):
        operating_deck = None
        if player == "player":
            operating_deck = self.player_deck.get_chosen()
        elif player == "opposite":
            operating_deck = self.opposite_deck.get_chosen()

        if self.valid_move(operating_deck, player, turn):
            # If valid move, then move old cards in current to discard
            self.move_to_discard()
            # move chosen to current
            self.move_chosen_to_current(player)

            return True
            # return "success" / true
        else:
            return False

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
    def valid_move(self, operating_deck, player, turn):
        # Covers the case if the player has 4 double in a row, he can play it at anytime
        # If the current card is 2 or two 2's.
        if len(operating_deck) % 2 == 0 and len(operating_deck) >= 8 and player != turn:
            current_card = self.current_deck.get_deck()

            if len(current_card) > 2 and player != turn:
                return False
            elif len(current_card) == 2 or len(current_card) == 1:
                is_two = True

                for card in current_card:
                    is_two = is_two and card.get_value() == "2"

                if not is_two:
                    return False
                else:
                    return self.is_double_consecutive(operating_deck)

        # Else, if the player that is pressing the play button is not at his turn, then
        # he cannot make the move.
        if player != turn:
            return False

        # If there are no cards in the chosen deck, then he cannot make the move.
        if len(operating_deck) == 0:
            return False

        # Covers the case when it is the opening of the trick, i.e. The player is opening up
        # and there are no cards in current_deck.
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

                return valid

        # Covers the case when it is the middle of the trick. Here we have to compare card values, and
        # Deck size.
        else:
            current_deck = self.current_deck.get_deck()

            if self.current_deck.get_length() == 1:
                if current_deck[0].get_value() == "2":
                    if len(operating_deck) == 1:
                        if operating_deck[0].get_value() != "2":
                            if self.quad_beat_two(operating_deck) or self.triple_beat_two(operating_deck) or \
                                    self.special_beat_two(operating_deck):
                                return True

                            return False
                        else:
                            if compare(operating_deck[0], current_deck[0]) == "player":
                                return True
                            else:
                                return False
                    elif len(operating_deck) == 4:
                        if not is_same(operating_deck):
                            return False
                        else:
                            return True
                    elif len(operating_deck) == 3:
                        return False
                    elif len(operating_deck) % 2 == 0 and len(operating_deck) > 5:
                        return self.is_double_consecutive(operating_deck)
                    else:
                        return False
                else:
                    if compare(operating_deck[0], current_deck[0]) == "player":
                        return True
                    else:
                        return False

            elif self.current_deck.get_length() == 2:
                if current_deck[0].get_value() == "2":
                    if len(operating_deck) == 1:
                        return False
                    elif len(operating_deck) == 2:
                        if operating_deck[0].get_value() != "2":
                            if self.quad_beat_two(operating_deck) or self.special_beat_two(operating_deck):
                                return True
                            else:
                                return False
                        else:
                            if is_same(operating_deck):
                                if compare(operating_deck[1], current_deck[1]) == "player":
                                    return True
                                else:
                                    return False
                            else:
                                return False
                    elif len(operating_deck) == 4:
                        if operating_deck[0].get_value() != "2" or not is_same(operating_deck):
                            return False
                        else:
                            return True
                    elif len(operating_deck) % 2 == 0 and len(operating_deck) > 5:
                        return operating_deck[0].get_value() == "2" and self.is_double_consecutive(operating_deck)
                    else:
                        return False
                else:
                    if not is_same(operating_deck):
                        return False
                    else:
                        if compare(operating_deck[1], current_deck[1]) == "player":
                            return True
                        else:
                            return False

            elif self.current_deck.get_deck() == 3:
                if self.current_deck.get_length() != len(operating_deck):
                    return False

                if current_deck[0].get_value() == "2":
                    return False

                if self.is_consecutive(current_deck):
                    if not self.is_consecutive(operating_deck):
                        return False
                    else:
                        if compare(operating_deck[-1], current_deck[-1]) == "player":
                            return True
                        else:
                            return False
                elif is_same(current_deck):
                    if not is_same(operating_deck):
                        return False
                    else:
                        if compare(operating_deck[-1], current_deck[-1]) == "player":
                            return True
                        else:
                            return False

            elif self.current_deck.get_deck() == 4:
                if self.current_deck.get_length() != len(operating_deck):
                    return False

                if self.is_consecutive(current_deck):
                    if not self.is_consecutive(operating_deck):
                        return False
                    else:
                        if compare(operating_deck[-1], current_deck[-1]) == "player":
                            return True
                        else:
                            return False
                elif is_same(current_deck):
                    if not is_same(operating_deck):
                        return False
                    else:
                        if compare(operating_deck[-1], current_deck[-1]) == "player":
                            return True
                        else:
                            return False

            elif len(self.current_deck.get_deck()) > 4 and self.current_deck.get_length() % 2 == 0:
                if self.current_deck.get_length() != len(operating_deck):
                    return False

                if self.is_consecutive(current_deck):
                    if not self.is_consecutive(operating_deck):
                        return False
                    else:
                        if compare(operating_deck[-1], current_deck[-1]) == "player":
                            return True
                        else:
                            return False
                elif self.is_double_consecutive(current_deck):
                    if not self.is_double_consecutive(operating_deck):
                        return False
                    else:
                        if compare(operating_deck[-1], current_deck[-1]) == "player":
                            return True
                        else:
                            return False
            else:
                if self.current_deck.get_length() != len(operating_deck):
                    return False
                if self.is_consecutive(current_deck):
                    if not self.is_consecutive(operating_deck):
                        return False
                    else:
                        if compare(operating_deck[-1], current_deck[-1]) == "player":
                            return True
                        else:
                            return False

    def triple_beat_two(self, current_deck):
        if len(current_deck) == 6 and self.is_double_consecutive(current_deck):
            return True
        else:
            return False

    def quad_beat_two(self, current_deck):
        if len(current_deck) == 4 and is_same(current_deck):
            return True
        else:
            return False

    def special_beat_two(self, current_deck):
        if len(current_deck) >= 6 and len(current_deck) % 2 == 0 and self.is_double_consecutive(current_deck):
            return True
        else:
            return False

    def is_consecutive(self, operating_deck):
        if operating_deck[-1].get_value() == "2":
            return False

        i = 1
        while i < len(operating_deck):
            if to_int_value(operating_deck[i - 1].get_value()) >= to_int_value(operating_deck[i].get_value()):
                return False

            i += 1

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

    def transfer_board(self, server_board):
        self.random = Random()
        self.shuffledeck.transfer_all_cards_to_deck(server_board.shuffledeck.get_deck())

        if self.player_id == 1:
            self.player_deck.transfer_all_cards_to_deck(server_board.player_deck.get_deck())
            self.opposite_deck.transfer_all_cards_to_deck(server_board.opposite_deck.get_deck())
        else:
            self.player_deck.transfer_all_cards_to_deck(server_board.opposite_deck.get_deck())
            self.opposite_deck.transfer_all_cards_to_deck(server_board.player_deck.get_deck())

        self.current_deck.transfer_all_cards_to_deck(server_board.current_deck.get_deck())
        self.discard_deck.transfer_all_cards_to_deck(server_board.discard_deck.get_deck())
