import math
import random
import pygame
from Cards import Cards
from Settings import Settings


def update_rect(rect, x, y, width, height):
    return rect.update(x, y, width, height)


class Board2:
    def __init__(self, screen):
        self.screen = screen
        self.settings = Settings()

        # The layout of the board
        # The player's Deck
        self.player_deck = []
        # The opponent's Deck
        self.opponent_deck = []
        # The current play deck: where we will place the cards
        # That are currently being played.
        self.current_play_pile = []
        # The Discard pile
        self.discard_deck_pile = []

        # Opponent chosen card(s)
        self.opponent_chosen = []
        # Player chosen card(s)
        self.player_chosen = []

        self.opponent_deck_x = 50
        self.opponent_deck_y = 75

        self.player_deck_x = 50
        self.player_deck_y = 675

        self.play_deck_width = 800

        self.player_chosen_height = 600
        self.opponent_chosen_height = 150

        self.current_play_pile_x = 250
        self.current_play_pile_y = 425

        self.discard_deck_pile_x = 750
        self.discard_deck_pile_y = 50

        self.deck = self.create_deck()

        self.deck_x = 450
        self.deck_y = 425

        self.opponent_deck_collide_point = pygame.Rect(self.opponent_deck_x, self.opponent_deck_y,
                                                       0, 0)
        self.player_deck_collide_point = pygame.Rect(self.player_deck_x, self.player_deck_y,
                                                     0, 0)

        self.card_width = 100
        self.card_height = 150

    # Method to reset the board
    def reset(self):
        self.player_deck = []
        self.opponent_deck = []
        self.current_play_pile = []
        self.discard_deck_pile = []
        self.opponent_chosen = []
        self.player_chosen = []

        self.deck = self.create_deck()
        self.opponent_deck_collide_point = pygame.Rect(self.opponent_deck_x, self.opponent_deck_y,
                                                       0, 0)
        self.player_deck_collide_point = pygame.Rect(self.player_deck_x, self.player_deck_y,
                                                     0, 0)
        self.draw_board()

    # Method to create the shuffled deck to begin dealing
    def create_deck(self):
        deck = [Cards(self.screen, "A", "Spades",
                      "Assets/card-spades-1.png", "Assets/card-back1.png"), Cards(self.screen, "2", "Spades",
                                                                                  "Assets/card-spades-2.png",
                                                                                  "Assets/card-back1.png"),
                Cards(self.screen, "3", "Spades",
                      "Assets/card-spades-3.png", "Assets/card-back1.png"), Cards(self.screen, "4", "Spades",
                                                                                  "Assets/card-spades-4.png",
                                                                                  "Assets/card-back1.png"),
                Cards(self.screen, "5", "Spade",
                      "Assets/card-spades-5.png", "Assets/card-back1.png"), Cards(self.screen, "6", "Spades",
                                                                                  "Assets/card-spades-6.png",
                                                                                  "Assets/card-back1.png"),
                Cards(self.screen, "7", "Spades",
                      "Assets/card-spades-7.png", "Assets/card-back1.png"), Cards(self.screen, "8", "Spades",
                                                                                  "Assets/card-spades-8.png",
                                                                                  "Assets/card-back1.png"),
                Cards(self.screen, "9", "Spades",
                      "Assets/card-spades-9.png", "Assets/card-back1.png"), Cards(self.screen, "10", "Spades",
                                                                                  "Assets/card-spades-10.png",
                                                                                  "Assets/card-back1.png"),
                Cards(self.screen, "J", "Spades",
                      "Assets/card-spades-11.png", "Assets/card-back1.png"), Cards(self.screen, "Q", "Spades",
                                                                                   "Assets/card-spades-12.png",
                                                                                   "Assets/card-back1.png"),
                Cards(self.screen, "K", "Spades",
                      "Assets/card-spades-13.png", "Assets/card-back1.png"), Cards(self.screen, "A", "Clubs",
                                                                                   "Assets/card-clubs-1.png",
                                                                                   "Assets/card-back1.png"),
                Cards(self.screen, "2", "Clubs",
                      "Assets/card-clubs-2.png", "Assets/card-back1.png"), Cards(self.screen, "3", "Clubs",
                                                                                 "Assets/card-clubs-3.png",
                                                                                 "Assets/card-back1.png"),
                Cards(self.screen, "4", "Clubs",
                      "Assets/card-clubs-4.png", "Assets/card-back1.png"), Cards(self.screen, "5", "Clubs",
                                                                                 "Assets/card-clubs-5.png",
                                                                                 "Assets/card-back1.png"),
                Cards(self.screen, "6", "Clubs",
                      "Assets/card-clubs-6.png", "Assets/card-back1.png"), Cards(self.screen, "7", "Clubs",
                                                                                 "Assets/card-clubs-7.png",
                                                                                 "Assets/card-back1.png"),
                Cards(self.screen, "8", "Clubs",
                      "Assets/card-clubs-8.png", "Assets/card-back1.png"), Cards(self.screen, "9", "Clubs",
                                                                                 "Assets/card-clubs-9.png",
                                                                                 "Assets/card-back1.png"),
                Cards(self.screen, "10", "Clubs",
                      "Assets/card-clubs-10.png", "Assets/card-back1.png"), Cards(self.screen, "J", "Clubs",
                                                                                  "Assets/card-clubs-11.png",
                                                                                  "Assets/card-back1.png"),
                Cards(self.screen, "Q", "Clubs",
                      "Assets/card-clubs-12.png", "Assets/card-back1.png"), Cards(self.screen, "K", "Clubs",
                                                                                  "Assets/card-clubs-13.png",
                                                                                  "Assets/card-back1.png"),
                Cards(self.screen, "A", "Diamonds",
                      "Assets/card-diamonds-1.png", "Assets/card-back1.png"), Cards(self.screen, "2", "Diamonds",
                                                                                    "Assets/card-diamonds-2.png",
                                                                                    "Assets/card-back1.png"),
                Cards(self.screen, "3", "Diamonds",
                      "Assets/card-diamonds-3.png", "Assets/card-back1.png"), Cards(self.screen, "4", "Diamonds",
                                                                                    "Assets/card-diamonds-4.png",
                                                                                    "Assets/card-back1.png"),
                Cards(self.screen, "5", "Diamonds",
                      "Assets/card-diamonds-5.png", "Assets/card-back1.png"), Cards(self.screen, "6", "Diamonds",
                                                                                    "Assets/card-diamonds-6.png",
                                                                                    "Assets/card-back1.png"),
                Cards(self.screen, "7", "Diamonds",
                      "Assets/card-diamonds-7.png", "Assets/card-back1.png"), Cards(self.screen, "8", "Diamonds",
                                                                                    "Assets/card-diamonds-8.png",
                                                                                    "Assets/card-back1.png"),
                Cards(self.screen, "9", "Diamonds",
                      "Assets/card-diamonds-9.png", "Assets/card-back1.png"), Cards(self.screen, "10", "Diamonds",
                                                                                    "Assets/card-diamonds-10.png",
                                                                                    "Assets/card-back1.png"),
                Cards(self.screen, "J", "Diamonds",
                      "Assets/card-diamonds-11.png", "Assets/card-back1.png"), Cards(self.screen, "Q", "Diamonds",
                                                                                     "Assets/card-diamonds-12.png",
                                                                                     "Assets/card-back1.png"),
                Cards(self.screen, "K", "Diamonds",
                      "Assets/card-diamonds-13.png", "Assets/card-back1.png"), Cards(self.screen, "A", "Hearts",
                                                                                     "Assets/card-hearts-1.png",
                                                                                     "Assets/card-back1.png"),
                Cards(self.screen, "2", "Hearts",
                      "Assets/card-hearts-2.png", "Assets/card-back1.png"), Cards(self.screen, "3", "Hearts",
                                                                                  "Assets/card-hearts-3.png",
                                                                                  "Assets/card-back1.png"),
                Cards(self.screen, "4", "Hearts",
                      "Assets/card-hearts-4.png", "Assets/card-back1.png"), Cards(self.screen, "5", "Hearts",
                                                                                  "Assets/card-hearts-5.png",
                                                                                  "Assets/card-back1.png"),
                Cards(self.screen, "6", "Hearts",
                      "Assets/card-hearts-6.png", "Assets/card-back1.png"), Cards(self.screen, "7", "Hearts",
                                                                                  "Assets/card-hearts-7.png",
                                                                                  "Assets/card-back1.png"),
                Cards(self.screen, "8", "Hearts",
                      "Assets/card-hearts-8.png", "Assets/card-back1.png"), Cards(self.screen, "9", "Hearts",
                                                                                  "Assets/card-hearts-9.png",
                                                                                  "Assets/card-back1.png"),
                Cards(self.screen, "10", "Hearts",
                      "Assets/card-hearts-10.png", "Assets/card-back1.png"), Cards(self.screen, "J", "Hearts",
                                                                                   "Assets/card-hearts-11.png",
                                                                                   "Assets/card-back1.png"),
                Cards(self.screen, "Q", "Hearts",
                      "Assets/card-hearts-12.png", "Assets/card-back1.png"), Cards(self.screen, "K", "Hearts",
                                                                                   "Assets/card-hearts-13.png",
                                                                                   "Assets/card-back1.png")]

        return deck

    def draw_board(self):
        self.draw_deck("shuffle")
        self.draw_deck("opponent")
        self.draw_deck("current")
        self.draw_deck("discard")
        self.draw_deck("player")
        self.draw_deck("player-chosen")
        self.draw_deck("opponent-chosen")

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
    def draw_deck(self, deck_type):
        if deck_type == "shuffle":
            self.move_to_shuffle_pos()
            self.deck[0].draw(False)
        elif deck_type == "opponent":
            num_cards = len(self.opponent_deck)
            starting = (self.play_deck_width + self.opponent_deck_x) - (num_cards * self.card_width)
            starting = starting / 2
            card_pos = min(self.card_width,
                           round((self.play_deck_width - self.card_width) / (num_cards - 1)))

            update_rect(self.opponent_deck_collide_point, self.opponent_deck_x, self.opponent_deck_y,
                        (num_cards * self.card_width), self.card_height)

            for x in self.opponent_deck:
                if not x.get_chosen():
                    x.update_vis(False)
                    if x.cur_pos() == (self.deck_x, self.deck_y):
                        x.rotate(180)
                    x.move(starting, self.opponent_deck_y, False)
                    x.update_card_block_area(starting + card_pos, self.card_height,
                                             self.card_width - card_pos, self.card_height)
                    x.draw()

                starting += card_pos
        elif deck_type == "current":
            num_cards = len(self.current_play_pile)
            starting = (self.play_deck_width + self.current_play_pile_x) - (num_cards * self.card_width)
            starting = starting / 2

            for x in self.current_play_pile:
                x.update_vis(True)
                x.move(starting, self.current_play_pile_y, False)
                x.draw()

                starting += x.get_width()
        elif deck_type == "discard":
            for x in self.current_play_pile:
                x.move(self.discard_deck_pile_x, self.discard_deck_pile_y, False)
                x.update_vis(False)

            card = self.discard_deck_pile[len(self.discard_deck_pile) - 1]
            card.draw()
        elif deck_type == "player":
            num_cards = len(self.player_deck)
            starting = (self.play_deck_width + self.player_deck_x) - (num_cards * self.card_width)
            starting = starting / 2
            card_pos = min(self.card_width,
                           round((self.play_deck_width - self.card_width) / (num_cards - 1)))

            update_rect(self.player_deck_collide_point, self.player_deck_x, self.player_deck_y,
                        (num_cards * self.card_width), self.card_height)

            for x in self.player_deck:
                if not x.get_chosen():
                    x.update_vis(True)
                    x.move(starting, self.player_deck, False)
                    x.update_card_block_area(starting + card_pos, self.card_height,
                                             self.card_width - card_pos, self.card_height)
                    x.draw()

                starting += x.get_width()
        elif deck_type == "player-chosen":
            for card in self.player_chosen:
                x, y = card.cur_pos()
                card.move(x, self.player_chosen_height)

                num_cards = len(self.player_deck)
                card_pos = min(self.card_width,
                               round((self.play_deck_width - self.card_width) / (num_cards - 1)))
                original_x, original_y = card.cur_pos()
                card.update_card_block_area(original_x + card_pos,
                                            self.player_deck_y,
                                            self.card_width - card_pos,
                                            self.player_deck_y - self.player_chosen_height)
                card.draw()
        elif deck_type == "opponent-chosen":
            for card in self.opponent_chosen:
                x, y = card.cur_pos()
                card.move(x, self.opponent_chosen_height)
                num_cards = len(self.opponent_deck)
                card_pos = min(self.card_width,
                               round((self.play_deck_width - self.card_width) / (num_cards - 1)))
                original_x, original_y = card.cur_pos()
                card.update_card_block_area(original_x + card_pos,
                                            self.opponent_deck_y,
                                            self.card_width - card_pos,
                                            self.opponent_chosen_height - self.opponent_deck_y)
                card.draw()

    # Method to shuffle the deck
    def shuffle_deck(self):
        return random.shuffle(self.deck)

    # Method to deal the shuffled card.
    # takes in the winner of the last game.
    # deals in counter clock-wise
    # Must implement the move.
    def deal(self, last_winner):
        counter = 0
        if last_winner == "player 1":
            for card in self.deck:
                card.change_in_play(True)
                if counter % 2 == 0:
                    self.player_deck.append(card)
                    self.deck.remove(card)
                    self.draw_deck("player")
                else:
                    card.update_vis(False)
                    self.opponent_deck.append(card)
                    self.deck.remove(card)
                    self.draw_deck("opponent")
                counter += 1
        else:
            for card in self.deck:
                card.change_in_play(True)
                if counter % 2 == 1:
                    self.player_deck.append(card)
                    self.deck.remove(card)
                    self.draw_deck("player")
                else:
                    card.update_vis(False)
                    self.opponent_deck.append(card)
                    self.deck.remove(card)
                    self.draw_deck("opponent")
                counter += 1

    # Method to move card from play pile to chosen pile
    def move_play_to_chosen(self, card, deck_type):
        if deck_type == "player":
            card.change_chosen(True)
            self.player_chosen.append(card)

            self.draw_deck("player-chosen")
            self.draw_deck("player")
        if deck_type == "opponent":
            card.change_chosen(True)
            self.opponent_chosen.append(card)

            self.draw_deck("opponent-chosen")
            self.draw_deck("opponent")

    def move_chosen_to_play(self, card, deck_type):
        if deck_type == "player":
            card.change_chosen(False)
            self.player_chosen.remove(card)

            self.draw_deck("player-chosen")
            self.draw_deck("player")
        if deck_type == "opponent":
            card.change_chosen(False)
            self.opponent_chosen.remove(card)

            self.draw_deck("opponent-chosen")
            self.draw_deck("opponent")

    # Method to move card from pile to the play pile
    def move_chosen_to_current(self, pile_from, cards):
        if pile_from == "player":
            for card in cards:
                card.change_in_play(False)
                self.current_play_pile.append(card)
                self.player_chosen.remove(card)
                self.player_deck.remove(card)
                self.draw_deck("current")
                self.draw_deck("player")
        elif pile_from == "opponent":
            for card in cards:
                card.change_in_play(False)
                self.current_play_pile.append(card)
                self.opponent_chosen.remove(card)
                self.opponent_deck.remove(card)
                self.draw_deck("current")
                self.draw_deck("opponent")

    # Method to move card to the shuffle deck position
    def move_to_shuffle_pos(self):
        for x in self.deck:
            x.move(self.deck_x, self.deck_y, True)
            x.update_vis(False)

    # Method to move cards to the discard pile
    def move_to_discard(self):
        for card in self.current_play_pile:
            card.change_in_play(False)
            self.discard_deck_pile.append(card)
            self.draw_deck("discard")

        self.current_play_pile = []

    def draw_names(self):
        pass

    # Handle collision. Choosing a card. Passes in x and y position of mouse. First find which deck was chosen
    # and then go through every card in that deck to find the card. Move that card to the chosen
    def choose_card(self, mouse_x, mouse_y, cur_player):
        if self.opponent_deck_collide_point.collidepoint(mouse_x, mouse_y):
            deck_type = "opponent"
        elif self.player_deck_collide_point.collidepoint(mouse_x, mouse_y):
            deck_type = "player"
        else:
            for card in self.opponent_chosen:
                pass
