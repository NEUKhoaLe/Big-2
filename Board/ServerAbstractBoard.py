from random import Random

from Cards.Deck.Shuffle.ServerShuffleDeck import ServerShuffleDeck

from Cards.ServerCard import ServerCard
from Utils.ServerSettings import ServerSettings


def if_contains(args, word):
    for w in args:
        if w == word:
            return True

    return False


class ServerAbstractBoard:
    def __init__(self):
        self.settings = ServerSettings()
        self.random = Random()
        self.shuffledeck = ServerShuffleDeck(self.settings.shuffle_x, self.settings.shuffle_y,
                                             deck=self.create_deck())

    def reset(self):
        pass

    # Method to create the shuffled deck to begin dealing
    def create_deck(self):
        deck = [ServerCard("A", "Spades",
                           "Assets/card-spades-1.png", "Assets/card-back1.png"),
                ServerCard("2", "Spades",
                           "Assets/card-spades-2.png",
                           "Assets/card-back1.png"),
                ServerCard("3", "Spades",
                           "Assets/card-spades-3.png", "Assets/card-back1.png"),
                ServerCard("4", "Spades",
                           "Assets/card-spades-4.png",
                           "Assets/card-back1.png"),
                ServerCard("5", "Spade",
                           "Assets/card-spades-5.png", "Assets/card-back1.png"),
                ServerCard("6", "Spades",
                           "Assets/card-spades-6.png",
                           "Assets/card-back1.png"),
                ServerCard("7", "Spades",
                           "Assets/card-spades-7.png", "Assets/card-back1.png"),
                ServerCard("8", "Spades",
                           "Assets/card-spades-8.png",
                           "Assets/card-back1.png"),
                ServerCard("9", "Spades",
                           "Assets/card-spades-9.png", "Assets/card-back1.png"),
                ServerCard("10", "Spades",
                           "Assets/card-spades-10.png",
                           "Assets/card-back1.png"),
                ServerCard("J", "Spades",
                           "Assets/card-spades-11.png", "Assets/card-back1.png"),
                ServerCard("Q", "Spades",
                           "Assets/card-spades-12.png",
                           "Assets/card-back1.png"),
                ServerCard("K", "Spades",
                           "Assets/card-spades-13.png", "Assets/card-back1.png"),
                ServerCard("A", "Clubs",
                           "Assets/card-clubs-1.png",
                           "Assets/card-back1.png"),
                ServerCard("2", "Clubs",
                           "Assets/card-clubs-2.png", "Assets/card-back1.png"),
                ServerCard("3", "Clubs",
                           "Assets/card-clubs-3.png",
                           "Assets/card-back1.png"),
                ServerCard("4", "Clubs",
                           "Assets/card-clubs-4.png", "Assets/card-back1.png"),
                ServerCard("5", "Clubs",
                           "Assets/card-clubs-5.png",
                           "Assets/card-back1.png"),
                ServerCard("6", "Clubs",
                           "Assets/card-clubs-6.png", "Assets/card-back1.png"),
                ServerCard("7", "Clubs",
                           "Assets/card-clubs-7.png",
                           "Assets/card-back1.png"),
                ServerCard("8", "Clubs",
                           "Assets/card-clubs-8.png", "Assets/card-back1.png"),
                ServerCard("9", "Clubs",
                           "Assets/card-clubs-9.png",
                           "Assets/card-back1.png"),
                ServerCard("10", "Clubs",
                           "Assets/card-clubs-10.png", "Assets/card-back1.png"),
                ServerCard("J", "Clubs",
                           "Assets/card-clubs-11.png",
                           "Assets/card-back1.png"),
                ServerCard("Q", "Clubs",
                           "Assets/card-clubs-12.png", "Assets/card-back1.png"),
                ServerCard("K", "Clubs",
                           "Assets/card-clubs-13.png",
                           "Assets/card-back1.png"),
                ServerCard("A", "Diamonds",
                           "Assets/card-diamonds-1.png", "Assets/card-back1.png"),
                ServerCard("2", "Diamonds",
                           "Assets/card-diamonds-2.png",
                           "Assets/card-back1.png"),
                ServerCard("3", "Diamonds",
                           "Assets/card-diamonds-3.png", "Assets/card-back1.png"),
                ServerCard("4", "Diamonds",
                           "Assets/card-diamonds-4.png",
                           "Assets/card-back1.png"),
                ServerCard("5", "Diamonds",
                           "Assets/card-diamonds-5.png", "Assets/card-back1.png"),
                ServerCard("6", "Diamonds",
                           "Assets/card-diamonds-6.png",
                           "Assets/card-back1.png"),
                ServerCard("7", "Diamonds",
                           "Assets/card-diamonds-7.png", "Assets/card-back1.png"),
                ServerCard("8", "Diamonds",
                           "Assets/card-diamonds-8.png",
                           "Assets/card-back1.png"),
                ServerCard("9", "Diamonds",
                           "Assets/card-diamonds-9.png", "Assets/card-back1.png"),
                ServerCard("10", "Diamonds",
                           "Assets/card-diamonds-10.png",
                           "Assets/card-back1.png"),
                ServerCard("J", "Diamonds",
                           "Assets/card-diamonds-11.png", "Assets/card-back1.png"),
                ServerCard("Q", "Diamonds",
                           "Assets/card-diamonds-12.png",
                           "Assets/card-back1.png"),
                ServerCard("K", "Diamonds",
                           "Assets/card-diamonds-13.png", "Assets/card-back1.png"),
                ServerCard("A", "Hearts",
                           "Assets/card-hearts-1.png",
                           "Assets/card-back1.png"),
                ServerCard("2", "Hearts",
                           "Assets/card-hearts-2.png", "Assets/card-back1.png"),
                ServerCard("3", "Hearts",
                           "Assets/card-hearts-3.png",
                           "Assets/card-back1.png"),
                ServerCard("4", "Hearts",
                           "Assets/card-hearts-4.png", "Assets/card-back1.png"),
                ServerCard("5", "Hearts",
                           "Assets/card-hearts-5.png",
                           "Assets/card-back1.png"),
                ServerCard("6", "Hearts",
                           "Assets/card-hearts-6.png", "Assets/card-back1.png"),
                ServerCard("7", "Hearts",
                           "Assets/card-hearts-7.png",
                           "Assets/card-back1.png"),
                ServerCard("8", "Hearts",
                           "Assets/card-hearts-8.png", "Assets/card-back1.png"),
                ServerCard("9", "Hearts",
                           "Assets/card-hearts-9.png",
                           "Assets/card-back1.png"),
                ServerCard("10", "Hearts",
                           "Assets/card-hearts-10.png", "Assets/card-back1.png"),
                ServerCard("J", "Hearts",
                           "Assets/card-hearts-11.png",
                           "Assets/card-back1.png"),
                ServerCard("Q", "Hearts",
                           "Assets/card-hearts-12.png",
                           "Assets/card-back1.png"),
                ServerCard("K", "Hearts",
                           "Assets/card-hearts-13.png",
                           "Assets/card-back1.png")]

        return deck

    def shuffle_deck(self):
        self.shuffledeck.shuffle()

    # Method to move card to the shuffle deck position
    def move_to_shuffle_pos(self):
        self.shuffledeck.change_pos(0, 0, to_shuffle=True)
        self.shuffledeck.move_deck()
