import pygame
from Cards import Cards
from Settings import Settings
from Buttons import Buttons


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






