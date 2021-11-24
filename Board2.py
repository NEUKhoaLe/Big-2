import random
import pygame
from Cards import Cards
from Settings import Settings


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

        self.opponent_deck_x = 250
        self.opponent_deck_y = 75

        self.player_deck_x = 250
        self.player_deck_y = 675

        self.current_play_pile_x = 250
        self.current_play_pile_y = 425

        self.discard_deck_pile_x = 750
        self.discard_deck_pile_y = 50

        self.deck = self.create_deck()

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

    # Method to draw a given deck given a deck type
    # If it is a shuffle deck: we will draw only the top back
    # of the card
    # If it is the opponent's deck, then we will draw each card
    # moving to its place, reversed 180 degrees
    # If it is discard, we also only draw the top of the deck
    # card back
    # If it is the current play pile, we draw the card front
    def draw_deck(self, deck_type):
        if deck_type == "shuffle":
            for x in self.deck:
                x.move(450, 425, True)
            self.deck[0].draw(False)
        elif deck_type == "opponent":
            num_cards = len(self.opponent_deck)
            starting = 500 - (num_cards * self.opponent_deck[0].get_width())
            starting = starting / 2

            for x in self.opponent_deck:
                x.rotate(180, False)
                x.update_vis(False)
                x.move(starting, self.opponent_deck_y)
                x.draw()

                starting += x.get_width()
        elif deck_type == "current":
            num_cards = len(self.current_play_pile)
            starting = 500 - (num_cards * self.current_play_pile[0].get_width())
            starting = starting/2

            for x in self.current_play_pile:
                x.update_vis(True)
                x.move(starting, self.current_play_pile_y)
                x.draw()

                starting += x.get_width()
        elif deck_type == "discard":
            card = self.discard_deck_pile[len(self.discard_deck_pile)]
            card.move(self.discard_deck_pile_x, self.discard_deck_pile_y)
            card.draw()
        elif deck_type == "player":
            num_cards = len(self.player_deck)
            starting = 500 - (num_cards * self.player_deck[0].get_width())
            starting = starting / 2

            for x in self.player_deck:
                x.update_vis(True)
                x.move(starting, self.player_deck)
                x.draw()

                starting += x.get_width()

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
            for x in self.deck:
                if counter % 2 == 0:
                    self.player_deck.append(x)
                    self.deck.remove(x)
                else:
                    self.opponent_deck.append(x)
                    self.deck.remove(x)
                counter += 1
        else:
            for x in self.deck:
                if counter % 2 == 1:
                    self.player_deck.append(x)
                    self.deck.remove(x)
                else:
                    x.update_vis(False)
                    self.opponent_deck.append(x)
                    self.deck.remove(x)
                counter += 1

    # Method to move cards to the discard pile
    def move_to_discard(self):
        for x in self.current_play_pile:
            x.move(self.discard_deck_pile_x, self.discard_deck_pile_y)
            x.update_vis(False)
            self.discard_deck_pile.append(x)

        self.current_play_pile = []

    def draw_names(self):
        pass
