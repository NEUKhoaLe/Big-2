from Game.AbstractGame import AbstractGame
from Utils.Buttons import Buttons


class Game2Online(AbstractGame):
    def __init__(self, game_id):
        super().__init__(None)

        self.display = None
        self.surface = None

        self.turn = "player"
        self.have_selected_card_drag = False

        self.game_id = game_id

        self.player1 = None
        self.player2 = None

        self.server_ready = False

        # The Play button
        self.play_button = Buttons("  Play  ", self.settings.game_button_font,
                                   self.settings.play_button_x, self.settings.play_button_y, self.surface)
        # The Skip button
        self.skip_button = Buttons("  Skip  ", self.settings.game_button_font,
                                   self.settings.skip_button_x, self.settings.skip_button_y, self.surface)


