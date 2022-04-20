import sys

import pygame

from Board.Board2.Board2 import Board2
from Bots.EasyBot import EasyBot
from Game.AbstractGame import AbstractGame
from Game.Player import Player
from Utils.Buttons import Buttons
from Utils.Message import Message


class Game2Bot(AbstractGame):
    def __init__(self, win):
        super().__init__(win)

        self.surface = pygame.surface.Surface((self.settings.screen_width, self.settings.screen_height))
        self.surface.fill(self.settings.bg_color)

        self.game_message = Message(self.surface, self.display)

        # The player here will be player 1
        self.player1 = Player(self.surface, player_type="player")
        self.player2 = Player(self.surface, player_type="opposite")

        self.board = Board2(self.display, self.surface)

        self.turn = "player"

        self.player_skip = False
        self.opposite_skip = False

        self.current_play = None

        self.have_selected_card_drag = False

        self.end = False

        # The Play button
        self.play_button = Buttons("  Play  ", self.settings.game_button_font,
                                   self.settings.play_button_x, self.settings.play_button_y, self.surface)
        # The Skip button
        self.skip_button = Buttons("  Skip  ", self.settings.game_button_font,
                                   self.settings.skip_button_x, self.settings.skip_button_y, self.surface)

        self.replay_button = Buttons("  Play Again  ", self.settings.button_font,
                                     500, 500, self.display)

        self.quit_button = Buttons("  Quit  ", self.settings.button_font,
                                   500, 700, self.display)

        self.display.fill(self.settings.bg_color)

    def create_player(self, player1_name, player2):
        self.clear()

        if type(player1_name) is str:
            self.player1 = Player(self.surface, player_type="player")
            self.player1.enter_name(player1_name)
        else:
            self.player1 = player1_name

        if type(player2) is str:
            if player2 == "easy bot":
                self.player2 = EasyBot(self.surface, player2, "opposite")
        else:
            self.player2 = player2

        self.board = Board2(self.display, self.surface)
        self.player2.add_board(self.board)

        self.draw_player_name()

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
            self.player2.draw_name()
        # elif type(self.player1) is HardBot:
        # pass

    def start_game(self):
        self.deal()
        # self.update(p=False, o=False)

    # Dealing The Card
    def deal(self):
        # self.board.shuffle_deck()
        self.board.move_to_shuffle_pos(game_update=False)
        self.board.deal(self.turn)

    def game_status(self):
        # check whether either player has won
        # check whether the player has a valid move
        if not self.end:
            winner = self.board.check_winner()
        else:
            winner = "none"

        if winner == "none":
            pass
        else:
            if winner == "player":
                self.player1.enter_score(self.player1.get_score() + 1)

                winner_font = self.settings.big2_font
                winner_render = winner_font.render(self.player1.get_name() + " is the Winner!", True, (255, 255, 255))
                winner_size = winner_font.size(self.player1.get_name() + " is the Winner!")

                self.surface.fill(self.settings.bg_color)
                self.surface.blit(winner_render, (500 - winner_size[0] / 2, 200 - winner_size[1] / 2))
                self.display.blit(self.surface, (0, 0))

                pygame.display.flip()

                self.replay_button.draw_button()
                self.quit_button.draw_button()

                self.end = True
                self.turn = "player"
            elif winner == "opposite":
                self.player2.enter_score(self.player2.get_score() + 1)

                winner_font = self.settings.big2_font
                winner_render = winner_font.render(self.player2.get_name() + " is the Winner!", True, (255, 255, 255))
                winner_size = winner_font.size(self.player2.get_name() + " is the Winner!")

                self.surface.fill(self.settings.bg_color)
                self.surface.blit(winner_render, (500 - winner_size[0] / 2, 200 - winner_size[1] / 2))

                pygame.display.flip()

                self.replay_button.draw_button()
                self.quit_button.draw_button()

                self.end = True
                self.turn = "opposite"

    # Selecting a card/un-selecting cards, and or board buttons
    def select(self, mouse_x, mouse_y):
        if self.end:
            if self.quit_button.collide_point(mouse_x, mouse_y):
                sys.exit()
            elif self.replay_button.collide_point(mouse_x, mouse_y):
                self.surface = pygame.surface.Surface((self.settings.screen_width, self.settings.screen_height))
                self.surface.fill(self.settings.bg_color)
                self.display.fill(self.settings.bg_color)

                self.board = Board2(self.display, self.surface)

                self.end = False
                self.quit_button.update_drawn(False)
                self.replay_button.update_drawn(False)

                self.player2.enter_surface(self.surface)
                self.player1.enter_surface(self.surface)

                self.start_game()
        else:
            if self.play_button.collide_point(mouse_x, mouse_y):
                success = self.board.play(self.turn, self.turn)
                # success = self.board.play("player", self.turn)
                if success:
                    # self.current_play = "player"
                    self.current_play = self.turn

                    self.change_turn()

                    self.game_message.draw_message("Successfully Play move. " + self.turn + " turn now.")

                    return self.turn
                else:
                    self.game_message.draw_message("Cannot play this hand.")
            elif self.skip_button.collide_point(mouse_x, mouse_y):
                self.change_turn()

                # This means that the current play has go around and should reset
                if self.current_play == self.turn:
                    self.game_message.draw_message("Trick completed. New round. " + self.turn + " turn now.")

                    self.board.move_to_discard()
                else:
                    self.game_message.draw_message("Previous player skipped turn. " + self.turn + " turn now.")

                return "skip"

            else:
                return self.board.choose_card(mouse_x, mouse_y, self.turn, False)
        # self.update()

    # Updating the game
    # Draw the board
    # Draw the player's .display.flip()names
    # Draw the buttons
    def update(self, s=True, o=True, c=True, d=True, l=True, r=True, p=True, gu=False):
        if not self.end:
            self.draw_player_name()
            self.skip_button.draw_button()
            self.play_button.draw_button()
            self.board.draw_board(shuffle=s, opposite=o, current=c, discard=d, player=p, left=l, right=r, gu=gu)
        else:
            self.replay_button.draw_button()
            self.quit_button.draw_button()

    def clear(self):
        self.surface.fill(self.settings.bg_color)

    def change_turn(self):
        if self.turn == "player":
            self.turn = "opposite"
        elif self.turn == "opposite":
            self.turn = "player"

    def get_turn(self):
        return self.turn

    def dragging_card(self, mouse_x, mouse_y, dragging):
        if not self.have_selected_card_drag and dragging:
            answer = self.board.choose_card(mouse_x, mouse_y, self.turn, dragging)
            if answer == "Not Selected player" or answer == "Not Selected opposite":
                self.have_selected_card_drag = False
                return "nothing"
            else:
                self.have_selected_card_drag = True

        if dragging and self.have_selected_card_drag:
            self.board.move_to_mouse(mouse_x, mouse_y, self.turn)

        if not dragging:
            if self.have_selected_card_drag:
                self.board.undrag(mouse_x, mouse_y, self.turn)
                self.have_selected_card_drag = False
            else:
                return "nothing"
