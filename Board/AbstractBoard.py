import random
import pygame
from Cards.Cards import Cards
from Utils.Settings import Settings


def update_rect(rect, x, y, width, height):
    return rect.update(x, y, width, height)


class AbstractBoard:
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

        self.opponent_deck_x = 250
        self.opponent_deck_y = 75

        self.player_deck_x = 250
        self.player_deck_y = 675

        self.play_deck_width = 500

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

    # Draw the board
    def draw_board(self):
        self.draw_deck("shuffle")
        self.draw_deck("opponent")
        self.draw_deck("current")
        self.draw_deck("discard")
        self.draw_deck("player")
        self.draw_deck("player-chosen")
        self.draw_deck("opponent-chosen")

    def draw_deck(self, deck_type):
        pass

    # Method to shuffle the deck
    def shuffle_deck(self):
        return random.shuffle(self.deck)

    def deal(self, last_winner):
        pass

    def move_play_to_chosen(self, card, deck_type):
        pass

    def move_chosen_to_play(self, card, deck_type):
        pass

    def move_chosen_to_current(self, pile_from, cards):
        pass

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

    def flip_vis(self, deck_type, boolean):
        pass

    def choose_card(self, mouse_x, mouse_y, cur_player):
        pass