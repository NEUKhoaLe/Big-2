import pygame

from Board.Board2 import Board2
from Bots.EasyBot import EasyBot
from Game.AbstractGame import AbstractGame
from Game.Player import Player
from Utils.Buttons import Buttons


class Game2Bot(AbstractGame):
    def __init__(self, win):

        super().__init__(win)

        self.surface = pygame.surface.Surface((self.settings.screen_width, self.settings.screen_height))
        self.surface.fill(self.settings.bg_color)

        # The player here will be player 1
        self.player1 = Player(self.surface, player_type="player")
        self.player2 = Player(self.surface, player_type="opposite")

        self.board = Board2(self.display, self.surface, self.player1, self.player2)

        self.turn = "player"

        self.have_selected_card_drag = False

        # The Play button
        self.play_button = Buttons("  Play  ", self.settings.game_button_font,
                                   self.settings.play_button_x, self.settings.play_button_y, self.surface)
        # The Skip button
        self.skip_button = Buttons("  Skip  ", self.settings.game_button_font,
                                   self.settings.skip_button_x, self.settings.skip_button_y, self.surface)

        player1_name = self.enter_name(self.surface)
        self.create_player(player1_name, "easy bot")

        self.display.fill(self.settings.bg_color)

    def enter_name(self, surface):
        entered_name1 = False
        player1_name = ""

        while not entered_name1:

            font = self.settings.game_mode_font

            surface.fill(self.settings.bg_color)
            pygame.display.flip()

            string_size = 0

            if not entered_name1:
                string = "Enter Player 1 name: " + player1_name
                title = font.render(string, True, (255, 255, 255))
                title_width = font.size(string)

                string_size = title_width[0]

                surface.blit(title, (500 - title_width[0]/2, 200 - title_width[1]/2))

            self.display.blit(surface, (0, 0))
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if not entered_name1 and player1_name != "":
                            entered_name1 = True
                    elif event.key == pygame.K_BACKSPACE:
                        if not entered_name1 and player1_name != "":
                            player1_name = player1_name[:-1]
                    else:
                        if not entered_name1 and not font.size(event.unicode)[0] + string_size >= 1000:
                            player1_name += event.unicode
                if entered_name1:
                    break

            pygame.display.flip()

        return player1_name

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

        self.board = Board2(self.display, self.surface, self.player1, self.player2)

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
            pass
        # elif type(self.player1) is HardBot:
        # pass

    def start_game(self):
        self.deal()
        # self.update(p=False, o=False)

    # Dealing The Card
    def deal(self):
        self.board.move_to_shuffle_pos(game_update=False)
        self.board.deal(self.turn)

    # Selecting a card/un-selecting cards, and or board buttons
    def select(self, mouse_x, mouse_y):
        if self.play_button.collide_point(mouse_x, mouse_y):
            self.board.play(self.turn)
        elif self.skip_button.collide_point(mouse_x, mouse_y):
            self.change_turn()
        else:
            return self.board.choose_card(mouse_x, mouse_y, self.turn, False)
        # self.update()

    # Updating the game
    # Draw the board
    # Draw the player's .display.flip()names
    # Draw the buttons
    def update(self, s=True, o=True, c=True, d=True, l=True, r=True, p=True, gu=False):
        self.draw_player_name()
        self.skip_button.draw_button()
        self.play_button.draw_button()
        self.board.draw_board(shuffle=s, opposite=o, current=c, discard=d, player=p, left=l, right=r, gu=gu)

    def clear(self):
        self.surface.fill(self.settings.bg_color)

    def play_hand(self):
        pass

    def quit(self):
        pass

    def change_turn(self):
        if self.turn == "player":
            self.turn = "opposite"
        elif self.turn == "opposite":
            self.turn = "player"

    def change_score(self):
        pass

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
