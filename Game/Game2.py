from Board.Board2 import Board2
from Game.AbstractGame import AbstractGame
from Player import Player
from Utils.Buttons import Buttons


class Game2(AbstractGame):
    def __init__(self, win):

        super().__init__(win)

        self.board = Board2(self.screen)

        # The player here will be player 1
        self.player1 = Player()
        self.player2 = Player()

        # The Play button
        self.play_button = Buttons("Play", self.settings.game_button_font,
                                   250, 525, self.screen)
        # The Skip button
        self.skip_button = Buttons("Skip", self.settings.game_button_font,
                                   450, 525, self.screen)

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

