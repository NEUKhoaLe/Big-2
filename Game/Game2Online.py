from Board.Board2.Board2 import Board2
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

        self.board = Board2(self.display, self.surface)

    def get_player(self, player_number):
        if player_number == 1:
            return self.player1.copy()
        elif player_number == 2:
            return self.player2.copy()

    def set_ready(self, boolean):
        self.server_ready = boolean

    def set_display_and_surface(self, display, surface):
        self.display = display
        self.surface = surface

    # If player number 2, player_deck = 2, opposite_deck = 1
    def swap_decks(self, player_number):
        if player_number == 1:
            order = [1, 2]
        else:
            order = [2, 1]

        self.board.rotate_deck(order)

    def reconcile(self, game_object, player_number, name=False):
        server_game = game_object[0]
        server_player = game_object[1]

        if player_number != server_player:
            return

        if name:
            if player_number == 1:
                if server_game.get_player(player_number).get_name() != self.player1.get_name():
                    self.player1.set_name(server_game.get_player(player_number).get_name())

            elif player_number == 2:
                if server_game.get_player(server_game).get_name() != self.player2.get_name():
                    self.player2.set_name(server_game.get_player(player_number).get_name())
        else:
            pass
