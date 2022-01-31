from Board.Board2.Board2 import Board2
from Bots.EasyBot import EasyBot
from Game.AbstractGame import AbstractGame
from Game.Player import Player
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

    def create_player(self, player1_name, player2):
        self.clear()

        if type(player1_name) is str:
            self.player1 = Player(self.surface, player_type="player")
            self.player1.enter_name(player1_name)
        else:
            self.player1 = player1_name

        if type(player2) is str:
            self.player2 = Player(self.surface, player_type="opposite")
            self.player2.enter_name(player2)
        else:
            self.player2 = player2

        self.board = Board2(self.display, self.surface)

        self.draw_player_name()

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

    def clear(self):
        self.surface.fill(self.settings.bg_color)

    def draw_player_name(self):
        if type(self.player1) is Player:
            self.player1.draw_name()
        elif type(self.player1) is EasyBot:
            pass
        # elif type(self.player1) is HardBot:
        # pass

        if type(self.player2) is Player:
            self.player2.draw_name()
        elif type(self.player2) is EasyBot:
            pass
        # elif type(self.player1) is HardBot:
        # pass

    def reconcile(self, game_object, player_number):
        server_game = game_object[0]
        server_player = game_object[1]

        if player_number != server_player:
            return

        # Transferring the constants
        self.turn = server_game.turn
        self.have_selected_card_drag = server_game.turn

        self.game_id = server_game.game_id
        self.server_ready = server_game.server_ready

        # Player Transfer
        self.board.transfer_board(server_game.get_board())
        # Board Transfer
