import pygame

from Board.Board2.Board2 import Board2
from Bots.EasyBot import EasyBot
from Game.AbstractGame import AbstractGame
from Game.Player import Player
from Utils.Buttons import Buttons
import copy


class Game2Online(AbstractGame):
    def __init__(self, display, game_id):
        super().__init__(display)

        self.surface = pygame.Surface((self.settings.screen_width, self.settings.screen_height))

        self.turn = "player"
        self.have_selected_card_drag = False

        self.game_id = game_id

        self.player1 = None
        self.player2 = None

        self.started = False

        self.server_ready = False

        # The Play button
        self.play_button = Buttons("  Play  ", self.settings.game_button_font,
                                   self.settings.play_button_x, self.settings.play_button_y, self.surface)
        # The Skip button
        self.skip_button = Buttons("  Skip  ", self.settings.game_button_font,
                                   self.settings.skip_button_x, self.settings.skip_button_y, self.surface)

        self.board = Board2(self.display, self.surface, player_id=self.game_id)

    def start_game(self):
        self.started = True
        self.deal()
        # self.update(p=False, o=False)

    # Dealing The Card
    def deal(self):
        self.board.move_to_shuffle_pos(game_update=False)
        self.board.deal(self.turn)

    def get_player(self, player_number):
        if player_number == 1:
            return copy.deepcopy(self.player1)
        elif player_number == 2:
            return copy.deepcopy(self.player2)

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

        # self.draw_player_name()

    def set_ready(self, boolean):
        self.server_ready = boolean

    def get_ready(self):
        return self.server_ready

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

        # Board Transfer
        # Only do when both player has joined
        if server_game.player2 is not None and server_game.player1 is not None:
            self.board.transfer_board(server_game.get_board())

        # Player Transfer

        if player_number == 1:
            if server_game.player1 is not None:
                if self.player1 is None:
                    self.player1 = Player(self.surface, player_type="player")
                    self.player1.enter_name(server_game.player1.get_name())
                    self.player1.enter_score(server_game.player1.get_score())
                else:
                    self.player1.enter_name(server_game.player1.get_name())
                    self.player1.enter_score(server_game.player1.get_score())

            if server_game.player2 is not None:
                if self.player2 is None:
                    self.player2 = Player(self.surface, player_type="opposite")
                    self.player2.enter_name(server_game.player2.get_name())
                    self.player2.enter_score(server_game.player2.get_score())
                else:
                    self.player2.enter_name(server_game.player2.get_name())
                    self.player2.enter_score(server_game.player2.get_score())
        elif player_number == 2:
            if server_game.player2 is not None:
                if self.player1 is None:
                    self.player1 = Player(self.surface, player_type="player")
                    self.player1.enter_name(server_game.player2.get_name())
                    self.player1.enter_score(server_game.player2.get_score())
                else:
                    self.player1.enter_name(server_game.player2.get_name())
                    self.player1.enter_score(server_game.player2.get_score())

            if server_game.player1 is not None:
                if self.player2 is None:
                    self.player2 = Player(self.surface, player_type="opposite")
                    self.player2.enter_name(server_game.player1.get_name())
                    self.player2.enter_score(server_game.player1.get_score())
                else:
                    self.player2.enter_name(server_game.player1.get_name())
                    self.player2.enter_score(server_game.player1.get_score())

    def get_board(self):
        return copy.deepcopy(self.board)

    # Updating the game
    # Draw the board
    # Draw the player's .display.flip()names
    # Draw the buttons
    def update(self, s=True, o=True, c=True, d=True, l=True, r=True, p=True, gu=False):
        self.draw_player_name()
        self.skip_button.draw_button()
        self.play_button.draw_button()
        self.board.draw_board(shuffle=s, opposite=o, current=c, discard=d, player=p, left=l, right=r, gu=gu)

    def execute_instructions(self, data):
        array = data.split(" ")

        if array[0] == "name":
            if array[2] == 1:
                self.create_player(array[1], None)
            else:
                self.create_player(None, array[1])
        elif array[0] == "start":
            self.start_game()

        return "done"
