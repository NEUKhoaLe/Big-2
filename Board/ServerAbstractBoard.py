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
        deck = [ServerCard("A", "Spades"),
                ServerCard("2", "Spades"),
                ServerCard("3", "Spades"),
                ServerCard("4", "Spades"),
                ServerCard("5", "Spade"),
                ServerCard("6", "Spades"),
                ServerCard("7", "Spades"),
                ServerCard("8", "Spades"),
                ServerCard("9", "Spades"),
                ServerCard("10", "Spades"),
                ServerCard("J", "Spades"),
                ServerCard("Q", "Spades"),
                ServerCard("K", "Spades"),
                ServerCard("A", "Clubs"),
                ServerCard("2", "Clubs"),
                ServerCard("3", "Clubs"),
                ServerCard("4", "Clubs"),
                ServerCard("5", "Clubs"),
                ServerCard("6", "Clubs"),
                ServerCard("7", "Clubs"),
                ServerCard("8", "Clubs"),
                ServerCard("9", "Clubs"),
                ServerCard("10", "Clubs"),
                ServerCard("J", "Clubs"),
                ServerCard("Q", "Clubs"),
                ServerCard("K", "Clubs"),
                ServerCard("A", "Diamonds"),
                ServerCard("2", "Diamonds"),
                ServerCard("3", "Diamonds"),
                ServerCard("4", "Diamonds"),
                ServerCard("5", "Diamonds"),
                ServerCard("6", "Diamonds"),
                ServerCard("7", "Diamonds"),
                ServerCard("8", "Diamonds"),
                ServerCard("9", "Diamonds"),
                ServerCard("10", "Diamonds"),
                ServerCard("J", "Diamonds"),
                ServerCard("Q", "Diamonds"),
                ServerCard("K", "Diamonds"),
                ServerCard("A", "Hearts"),
                ServerCard("2", "Hearts"),
                ServerCard("3", "Hearts"),
                ServerCard("4", "Hearts"),
                ServerCard("5", "Hearts"),
                ServerCard("6", "Hearts"),
                ServerCard("7", "Hearts"),
                ServerCard("8", "Hearts"),
                ServerCard("9", "Hearts"),
                ServerCard("10", "Hearts"),
                ServerCard("J", "Hearts"),
                ServerCard("Q", "Hearts"),
                ServerCard("K", "Hearts")]

        return deck

    def shuffle_deck(self):
        self.shuffledeck.shuffle()

    # Method to move card to the shuffle deck position
    def move_to_shuffle_pos(self):
        self.shuffledeck.change_pos(0, 0, to_shuffle=True)
        self.shuffledeck.move_deck()
