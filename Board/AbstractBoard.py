from random import Random

from Cards.Cards import Cards
from Cards.ShuffleDeck import ShuffleDeck
from Utils.Settings import Settings


def if_contains(args, word):
    for w in args:
        if w == word:
            return True

    return False


class AbstractBoard:
    def __init__(self, display, surface):
        self.display = display
        self.surface = surface
        self.settings = Settings()
        self.random = Random()

        self.shuffledeck = ShuffleDeck(self.settings.shuffle_x, self.settings.shuffle_y,
                                       self.display, self.surface, deck=self.create_deck())

        self.card_width = 100
        self.card_height = 150

    # Method to reset the board
    def reset(self):
        pass

    # Method to create the shuffled deck to begin dealing
    def create_deck(self):
        deck = [Cards(self.display, self.surface, "A", "Spades",
                      "Assets/card-spades-1.png", "Assets/card-back1.png"),
                Cards(self.display, self.surface, "2", "Spades",
                      "Assets/card-spades-2.png",
                      "Assets/card-back1.png"),
                Cards(self.display, self.surface, "3", "Spades",
                      "Assets/card-spades-3.png", "Assets/card-back1.png"),
                Cards(self.display, self.surface, "4", "Spades",
                      "Assets/card-spades-4.png",
                      "Assets/card-back1.png"),
                Cards(self.display, self.surface, "5", "Spade",
                      "Assets/card-spades-5.png", "Assets/card-back1.png"),
                Cards(self.display, self.surface, "6", "Spades",
                      "Assets/card-spades-6.png",
                      "Assets/card-back1.png"),
                Cards(self.display, self.surface, "7", "Spades",
                      "Assets/card-spades-7.png", "Assets/card-back1.png"),
                Cards(self.display, self.surface, "8", "Spades",
                      "Assets/card-spades-8.png",
                      "Assets/card-back1.png"),
                Cards(self.display, self.surface, "9", "Spades",
                      "Assets/card-spades-9.png", "Assets/card-back1.png"),
                Cards(self.display, self.surface, "10", "Spades",
                      "Assets/card-spades-10.png",
                      "Assets/card-back1.png"),
                Cards(self.display, self.surface, "J", "Spades",
                      "Assets/card-spades-11.png", "Assets/card-back1.png"),
                Cards(self.display, self.surface, "Q", "Spades",
                      "Assets/card-spades-12.png",
                      "Assets/card-back1.png"),
                Cards(self.display, self.surface, "K", "Spades",
                      "Assets/card-spades-13.png", "Assets/card-back1.png"),
                Cards(self.display, self.surface, "A", "Clubs",
                      "Assets/card-clubs-1.png",
                      "Assets/card-back1.png"),
                Cards(self.display, self.surface, "2", "Clubs",
                      "Assets/card-clubs-2.png", "Assets/card-back1.png"),
                Cards(self.display, self.surface, "3", "Clubs",
                      "Assets/card-clubs-3.png",
                      "Assets/card-back1.png"),
                Cards(self.display, self.surface, "4", "Clubs",
                      "Assets/card-clubs-4.png", "Assets/card-back1.png"),
                Cards(self.display, self.surface, "5", "Clubs",
                      "Assets/card-clubs-5.png",
                      "Assets/card-back1.png"),
                Cards(self.display, self.surface, "6", "Clubs",
                      "Assets/card-clubs-6.png", "Assets/card-back1.png"),
                Cards(self.display, self.surface, "7", "Clubs",
                      "Assets/card-clubs-7.png",
                      "Assets/card-back1.png"),
                Cards(self.display, self.surface, "8", "Clubs",
                      "Assets/card-clubs-8.png", "Assets/card-back1.png"),
                Cards(self.display, self.surface, "9", "Clubs",
                      "Assets/card-clubs-9.png",
                      "Assets/card-back1.png"),
                Cards(self.display, self.surface, "10", "Clubs",
                      "Assets/card-clubs-10.png", "Assets/card-back1.png"),
                Cards(self.display, self.surface, "J", "Clubs",
                      "Assets/card-clubs-11.png",
                      "Assets/card-back1.png"),
                Cards(self.display, self.surface, "Q", "Clubs",
                      "Assets/card-clubs-12.png", "Assets/card-back1.png"),
                Cards(self.display, self.surface, "K", "Clubs",
                      "Assets/card-clubs-13.png",
                      "Assets/card-back1.png"),
                Cards(self.display, self.surface, "A", "Diamonds",
                      "Assets/card-diamonds-1.png", "Assets/card-back1.png"),
                Cards(self.display, self.surface, "2", "Diamonds",
                      "Assets/card-diamonds-2.png",
                      "Assets/card-back1.png"),
                Cards(self.display, self.surface, "3", "Diamonds",
                      "Assets/card-diamonds-3.png", "Assets/card-back1.png"),
                Cards(self.display, self.surface, "4", "Diamonds",
                      "Assets/card-diamonds-4.png",
                      "Assets/card-back1.png"),
                Cards(self.display, self.surface, "5", "Diamonds",
                      "Assets/card-diamonds-5.png", "Assets/card-back1.png"),
                Cards(self.display, self.surface, "6", "Diamonds",
                      "Assets/card-diamonds-6.png",
                      "Assets/card-back1.png"),
                Cards(self.display, self.surface, "7", "Diamonds",
                      "Assets/card-diamonds-7.png", "Assets/card-back1.png"),
                Cards(self.display, self.surface, "8", "Diamonds",
                      "Assets/card-diamonds-8.png",
                      "Assets/card-back1.png"),
                Cards(self.display, self.surface, "9", "Diamonds",
                      "Assets/card-diamonds-9.png", "Assets/card-back1.png"),
                Cards(self.display, self.surface, "10", "Diamonds",
                      "Assets/card-diamonds-10.png",
                      "Assets/card-back1.png"),
                Cards(self.display, self.surface, "J", "Diamonds",
                      "Assets/card-diamonds-11.png", "Assets/card-back1.png"),
                Cards(self.display, self.surface, "Q", "Diamonds",
                      "Assets/card-diamonds-12.png",
                      "Assets/card-back1.png"),
                Cards(self.display, self.surface, "K", "Diamonds",
                      "Assets/card-diamonds-13.png", "Assets/card-back1.png"),
                Cards(self.display, self.surface, "A", "Hearts",
                      "Assets/card-hearts-1.png",
                      "Assets/card-back1.png"),
                Cards(self.display, self.surface, "2", "Hearts",
                      "Assets/card-hearts-2.png", "Assets/card-back1.png"),
                Cards(self.display, self.surface, "3", "Hearts",
                      "Assets/card-hearts-3.png",
                      "Assets/card-back1.png"),
                Cards(self.display, self.surface, "4", "Hearts",
                      "Assets/card-hearts-4.png", "Assets/card-back1.png"),
                Cards(self.display, self.surface, "5", "Hearts",
                      "Assets/card-hearts-5.png",
                      "Assets/card-back1.png"),
                Cards(self.display, self.surface, "6", "Hearts",
                      "Assets/card-hearts-6.png", "Assets/card-back1.png"),
                Cards(self.display, self.surface, "7", "Hearts",
                      "Assets/card-hearts-7.png",
                      "Assets/card-back1.png"),
                Cards(self.display, self.surface, "8", "Hearts",
                      "Assets/card-hearts-8.png", "Assets/card-back1.png"),
                Cards(self.display, self.surface, "9", "Hearts",
                      "Assets/card-hearts-9.png",
                      "Assets/card-back1.png"),
                Cards(self.display, self.surface, "10", "Hearts",
                      "Assets/card-hearts-10.png", "Assets/card-back1.png"),
                Cards(self.display, self.surface, "J", "Hearts",
                      "Assets/card-hearts-11.png",
                      "Assets/card-back1.png"),
                Cards(self.display, self.surface, "Q", "Hearts",
                      "Assets/card-hearts-12.png",
                      "Assets/card-back1.png"),
                Cards(self.display, self.surface, "K", "Hearts",
                      "Assets/card-hearts-13.png",
                      "Assets/card-back1.png")]

        return deck

    def draw_board(self, shuffle=True, opposite=True, current=True, discard=True, player=True, gu=True):
        if shuffle:
            self.draw_deck("shuffle", gu)
        if opposite:
            self.draw_deck("opposite", gu)
        if current:
            self.draw_deck("current", gu)
        if discard:
            self.draw_deck("discard", gu)
        if player:
            self.draw_deck("player", gu)

    def draw_deck(self, deck_type, game_update):
        pass

    # Method to shuffle the deck
    def shuffle_deck(self):
        self.shuffledeck.shuffle()

    def deal(self, last_winner):
        pass

    def move_play_to_chosen(self, card, deck_type):
        pass

    def move_chosen_to_play(self, card, deck_type):
        pass

    def move_chosen_to_current(self, pile_from, cards):
        pass

    # Method to move card to the shuffle deck position
    def move_to_shuffle_pos(self, game_update):
        self.shuffledeck.change_pos(0, 0, to_shuffle=True)
        self.shuffledeck.draw_deck(False, game_update=game_update)

    # Method to move cards to the discard pile
    def move_to_discard(self):
        pass

    def flip_vis(self, deck_type, boolean):
        pass

    def choose_card(self, mouse_x, mouse_y, cur_player, dragging):
        pass

    # swapping the position of each deck 90 degrees counter clockwise
    # 180 degrees for two player
    def rotate_deck(self):
        pass

    def play(self, turn):
        pass

    def valid_move(self, turn):
        pass

    def is_double(self, operating_deck):
        pass

    def is_consecutive(self, operating_deck):
        pass

    def is_consecutive_double(self, operating_deck):
        pass

    def move_to_mouse(self, mouse_x, mouse_y, turn):
        pass

    def undrag(self, mouse_x, mouse_y, turn):
        pass
