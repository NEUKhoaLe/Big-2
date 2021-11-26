import pygame
from Buttons import Buttons
from Settings import Settings
from Board2 import Board2
from Player import Player


class Game2:
    def __init__(self, win):

        self.settings = Settings()
        self.screen = win
        self.board = Board2(self.screen)

        # The player here will be player 1
        self.player1 = Player()
        self.player2 = Player()

        # The Play button
        self.play_button = Buttons("Play", self.settings.game_button_font,
                                   700, 700, self.screen)
        # The Skip button
        self.skip_button = Buttons("Skip", self.settings.game_button_font,
                                   700, 790, self.screen)

    # Enter name method
    def enter_name(self, player_type, name):
        pass

    # Dealing The Card
    def deal(self):
        pass

    # Selecting a card/un-selecting cards, and or board buttons
    def select(self):
        pass

    # Updating the game
    # Draw the board
    # Draw the player's names
    # Draw the buttons
    def update(self):
        pass

    def play_hand(self):
        pass

    def quit(self):
        pass

    def skip_turn(self):
        pass

    def change_turn(self):
        pass

    def change_score(self):
        pass

