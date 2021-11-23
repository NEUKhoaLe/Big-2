import pygame
from Buttons import Buttons
from Settings import Settings


class Game2:
    def __init__(self, win):

        self.settings = Settings()
        self.screen = win

        # The Play button
        self.play_button = Buttons("Play", self.settings.game_button_font,
                                   1050, 720, self.screen)
        # The Skip button
        self.skip_button = Buttons("Skip", self.settings.game_button_font,
                                   30, 720, self.screen)
        # The Quit button
        self.quit_button = Buttons("Quit", self.settings.game_button_font,
                                   30, 20, self.screen)

    # Dealing The Card
    def deal(self):
        pass

    # Selecting a card/un-selecting cards, and or board buttons
    def select(self):
        pass

    # Updating the game
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

