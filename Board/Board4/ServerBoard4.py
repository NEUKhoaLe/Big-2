import pygame

from Board.ServerAbstractBoard import ServerAbstractBoard
from Cards.Deck.Current.ServerCurrentDeck import ServerCurrentDeck
from Cards.Deck.Discard.ServerDiscardDeck import ServerDiscardDeck
from Cards.Deck.PlayDeck.Left.ServerLeftDeck import ServerLeftDeck
from Cards.Deck.PlayDeck.Opposite.ServerOppositeDeck import ServerOppositeDeck
from Cards.Deck.PlayDeck.Player.ServerPlayerDeck import ServerPlayerDeck
from Cards.Deck.PlayDeck.Right.ServerRightDeck import ServerRightDeck


def is_same(operating_deck):
    i = 0

    while i < len(operating_deck) - 1:
        if operating_deck[i].get_value() != operating_deck[i + 1].get_value():
            return False

    return True


class ServerBoard4(ServerAbstractBoard):
    def __init__(self):
        super().__init__()

        self.opposite_deck_deck_collide_point = pygame.Rect(self.settings.opposite_deck_4_x, self.settings.opposite_y,
                                                            0, 0)
        self.player_deck_deck_collide_point = pygame.Rect(self.settings.player_deck_4_x, self.settings.player_y,
                                                          0, 0)

        self.left_deck_deck_collide_point = pygame.Rect(self.settings.left_deck_4_x, self.settings.left_deck_4_y,
                                                        0, 0)
        self.right_deck_deck_collide_point = pygame.Rect(self.settings.right_deck_4_x, self.settings.right_deck_4_y, 0,
                                                         0)
        # The layout of the board
        # The player's Deck
        self.player_deck = ServerPlayerDeck(self.settings.player_deck_4_x, self.settings.player_y,
                                            self.settings.player_chosen_y, self.settings.play_deck_width_4,
                                            self.player_deck_deck_collide_point)
        # The opponent's Deck
        self.opposite_deck = ServerOppositeDeck(self.settings.opposite_deck_4_x, self.settings.opposite_y,
                                                self.settings.opposite_chosen_y, self.settings.play_deck_width_4,
                                                self.opposite_deck_deck_collide_point)

        self.left_deck = ServerLeftDeck(self.settings.left_deck_4_x, self.settings.left_deck_4_y,
                                        self.settings.left_chosen_4_x, self.settings.play_deck_width_4,
                                        self.left_deck_deck_collide_point)
        self.right_deck = ServerRightDeck(self.settings.right_deck_4_x, self.settings.right_deck_4_y,
                                          self.settings.right_chosen_4_x, self.settings.play_deck_width_4,
                                          self.right_deck_deck_collide_point)

        self.board_dict = {1: self.player_deck, 2: self.right_deck, 3: self.opposite_deck, 4: self.left_deck}

        # The current play deck: where we will place the cards
        # That are currently being played.
        self.current_deck = ServerCurrentDeck(self.settings.current_deck_4_x, self.settings.current_deck_y,
                                              self.settings.play_deck_width_4)
        # The Discard pile
        self.discard_deck = ServerDiscardDeck(self.settings.discard_deck_x_4, self.settings.discard_deck_y_4)

    # Method to deal the shuffled card.
    # takes in the winner of the last game.
    # deals in counter clock-wise
    # Must implement the move.
    def deal(self, last_winner):
        if last_winner == "player":
            counter = 0
            i = self.shuffledeck.get_length() - 1
            while i >= 0:
                self.shuffledeck.card_change_in_play(i, True)
                self.board_dict[counter % 4 + 1].add_card(self.shuffledeck.remove_card("last"))
                self.board_dict[counter % 4 + 1].draw_deck(True)
                counter += 1
                i -= 1
        elif last_winner == "right":
            counter = 1
            i = self.shuffledeck.get_length() - 1
            while i >= 0:
                self.shuffledeck.card_change_in_play(i, True)
                self.board_dict[counter % 4 + 1].add_card(self.shuffledeck.remove_card("last"))
                self.board_dict[counter % 4 + 1].draw_deck(True)
                counter += 1
                i -= 1
        elif last_winner == "opposite":
            counter = 2
            i = self.shuffledeck.get_length() - 1
            while i >= 0:
                self.shuffledeck.card_change_in_play(i, True)
                self.board_dict[counter % 4 + 1].add_card(self.shuffledeck.remove_card("last"))
                self.board_dict[counter % 4 + 1].draw_deck(True)
                counter += 1
                i -= 1

        elif last_winner == "left":
            counter = 3
            i = self.shuffledeck.get_length() - 1
            while i >= 0:
                self.shuffledeck.card_change_in_play(i, True)
                self.board_dict[counter % 4 + 1].add_card(self.shuffledeck.remove_card("last"))
                self.board_dict[counter % 4 + 1].draw_deck(True)
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
        elif pile_from == "left":
            pass
        elif pile_from == "right":
            pass

    # Method to flip the visibility.
    def flip_vis(self, deck_type, boolean):
        if deck_type == "opposite":
            self.opposite_deck.flip_vis(boolean)
        elif deck_type == "player":
            self.player_deck.flip_vis(boolean)
        elif deck_type == "left":
            self.left_deck.flip_vis(boolean)
        elif deck_type == "right":
            self.right_deck.flip_vis(boolean)

    def select_deck(self, mouse_x, mouse_y):
        if self.player_deck.select_deck(mouse_x, mouse_y):
            return "player"
        elif self.opposite_deck.select_deck(mouse_x, mouse_y):
            return "opposite"
        elif self.left_deck.select_deck(mouse_x, mouse_y):
            return "left"
        elif self.right_deck.select_deck(mouse_x, mouse_y):
            return "right"

    # Handle collision. Choosing a card. Passes in x and y position of mouse. First find which deck was chosen
    # and then go through every card in that deck to find the card. Move that card to the chosen
    # If a chosen card is selected, then it is "unchosen" i.e. removed from the chosen pile
    def choose_card(self, mouse_x, mouse_y, cur_player, dragging):
        if self.select_deck(mouse_x, mouse_y) == "player" and cur_player == "player":
            return self.player_deck.handle_selected(mouse_x, mouse_y, dragging)
        elif self.select_deck(mouse_x, mouse_y) == "opposite" and cur_player == "opposite":
            return self.opposite_deck.handle_selected(mouse_x, mouse_y, dragging)
        elif self.select_deck(mouse_x, mouse_y) == "left" and cur_player == "left":
            return self.left_deck.handle_selected(mouse_x, mouse_y, dragging)
        elif self.select_deck(mouse_x, mouse_y) == "right" and cur_player == "right":
            return self.right_deck.handle_selected(mouse_x, mouse_y, dragging)
        else:
            return "Not Selected " + cur_player

    def rotate_deck(self, order):
        player_temp = self.player_deck.get_deck()
        left_temp = self.left_deck.get_deck()
        right_temp = self.right_deck.get_deck()
        opposite_temp = self.opposite_deck.get_deck()

        if order == [1, 2, 3, 4]:
            pass
        elif order == [2, 3, 4, 1]:
            self.player_deck.transfer_all_cards_to_deck(right_temp)
            self.right_deck.transfer_all_cards_to_deck(opposite_temp)
            self.opposite_deck.transfer_all_cards_to_deck(left_temp)
            self.left_deck.transfer_all_cards_to_deck(player_temp)
        elif order == [3, 4, 1, 2]:
            self.player_deck.transfer_all_cards_to_deck(opposite_temp)
            self.right_deck.transfer_all_cards_to_deck(left_temp)
            self.opposite_deck.transfer_all_cards_to_deck(player_temp)
            self.left_deck.transfer_all_cards_to_deck(right_temp)
        elif order == [4, 1, 2, 3]:
            self.player_deck.transfer_all_cards_to_deck(left_temp)
            self.right_deck.transfer_all_cards_to_deck(player_temp)
            self.opposite_deck.transfer_all_cards_to_deck(right_temp)
            self.left_deck.transfer_all_cards_to_deck(opposite_temp)

    def move_to_discard(self):
        pass

    def play(self, turn):
        operating_deck = None
        if turn == "player":
            operating_deck = self.player_deck.get_chosen()
        elif turn == "opposite":
            operating_deck = self.opposite_deck.get_chosen()
        elif turn == "left":
            operating_deck = self.left_deck.get_chosen()
        elif turn == "right":
            operating_deck = self.right_deck.get_chosen()

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
            if operating_deck[i - 1].get_value() != operating_deck[i].get_value() + 1:
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
        elif turn == "left":
            self.left_deck.move_to_mouse(mouse_x, mouse_y)
        elif turn == "right":
            self.right_deck.move_to_mouse(mouse_x, mouse_y)

    def undrag(self, mouse_x, mouse_y, turn):
        if turn == "player":
            self.player_deck.undrag(mouse_x, mouse_y)
        elif turn == "opposite":
            self.opposite_deck.undrag(mouse_x, mouse_y)
        elif turn == "left":
            self.left_deck.undrag(mouse_x, mouse_y)
        elif turn == "right":
            self.right_deck.undrag(mouse_x, mouse_y)

