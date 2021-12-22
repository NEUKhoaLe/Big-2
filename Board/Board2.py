import pygame

from Board.AbstractBoard import AbstractBoard
from Cards.CurrentDeck import CurrentDeck
from Cards.DiscardDeck import DiscardDeck
from Cards.OpponentDeck import OpponentDeck
from Cards.PlayerDeck import PlayerDeck


class Board2(AbstractBoard):
    def __init__(self, display, surface):
        super().__init__(display, surface)

        self.opponent_deck_collide_point = pygame.Rect(self.settings.opponent_deck_2_x, self.settings.opponent_y,
                                                       0, 0)
        self.player_deck_collide_point = pygame.Rect(self.settings.player_deck_2_x, self.settings.player_y,
                                                     0, 0)

        # The layout of the board
        # The player's Deck
        self.player_deck = PlayerDeck(self.settings.player_deck_2_x, self.settings.player_y,
                                      self.settings.player_chosen_y, self.settings.play_deck_width_2,
                                      self.player_deck_collide_point, self.display, self.surface)
        # The opponent's Deck
        self.opponent_deck = OpponentDeck(self.settings.opponent_deck_2_x, self.settings.opponent_y,
                                          self.settings.opponent_chosen_y, self.settings.play_deck_width_2,
                                          self.opponent_deck_collide_point, self.display, self.surface)
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
        elif deck_type == "opponent":
            self.opponent_deck.draw_deck(False, game_update)
        elif deck_type == "player":
            self.player_deck.draw_deck(False, game_update)
        elif deck_type == "current":
            self.current_deck.draw_deck(False, game_update)
        elif deck_type == "discard":
            self.discard_deck.draw_deck(False, game_update)

    # Method to deal the shuffled card.
    # takes in the winner of the last game.
    # deals in counter clock-wise
    # Must implement the move.
    def deal(self, last_winner):
        counter = 0
        if last_winner == "player 1":
            i = self.shuffledeck.get_length() - 1
            while i >= 0:
                self.shuffledeck.card_change_in_play(i, True)
                if counter % 2 == 0:
                    self.player_deck.add_card(self.shuffledeck.remove_card("last"))
                    self.player_deck.draw_deck(True)
                else:
                    self.opponent_deck.add_card(self.shuffledeck.remove_card("last"))
                    self.opponent_deck.draw_deck(True)
                counter += 1
                i -= 1
        else:
            i = self.shuffledeck.get_length() - 1
            while i >= 0:
                self.shuffledeck.card_change_in_play(i, True)
                if counter % 2 == 1:
                    self.opponent_deck.add_card(self.shuffledeck.remove_card("last"))
                    self.opponent_deck.draw_deck(True)
                else:
                    self.player_deck.add_card(self.shuffledeck.remove_card("last"))
                    self.player_deck.draw_deck(True)
                counter += 1
                i -= 1

    # Method to move card from play pile to chosen pile
    def move_play_to_chosen(self, card, deck_type):
        pass

    def move_chosen_to_play(self, card, deck_type):
        pass

    # Method to move card from pile to the play pile
    def move_chosen_to_current(self, pile_from, cards):
        if pile_from == "player":
            pass
        elif pile_from == "opponent":
            pass

    # Method to flip the visibility.
    def flip_vis(self, deck_type, boolean):
        if deck_type == "opponent":
            self.opponent_deck.flip_vis(boolean)
        elif deck_type == "player":
            self.player_deck.flip_vis(boolean)

    def select_deck(self, mouse_x, mouse_y):
        if self.player_deck.select_deck(mouse_x, mouse_y):
            return "player"
        elif self.opponent_deck.select_deck(mouse_x, mouse_y):
            return "opponent"

    # Handle collision. Choosing a card. Passes in x and y position of mouse. First find which deck was chosen
    # and then go through every card in that deck to find the card. Move that card to the chosen
    # If a chosen card is selected, then it is "unchosen" i.e. removed from the chosen pile
    def choose_card(self, mouse_x, mouse_y, cur_player):
        if self.select_deck(mouse_x, mouse_y) == "player":
            self.player_deck.handle_selected(mouse_x, mouse_y)
        elif self.select_deck(mouse_x, mouse_y) == "opponent":
            self.opponent_deck.handle_selected(mouse_x, mouse_y)

    def rotate_deck(self):
        temp_x, temp_y = self.opponent_deck.get_pos()

        self.opponent_deck.change_pos(self.player_deck.get_pos()[0], self.player_deck.get_pos()[1])
        self.player_deck.change_pos(temp_x, temp_y)

    def move_to_discard(self):
        pass
