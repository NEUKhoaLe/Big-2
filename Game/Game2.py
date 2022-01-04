from Board.Board2 import Board2
from Game.AbstractGame import AbstractGame
from Game.Player import Player
from Utils.Buttons import Buttons
import pygame


class Game2(AbstractGame):
    def __init__(self, win):

        super().__init__(win)

        self.surface = pygame.surface.Surface((self.settings.screen_width, self.settings.screen_height))
        self.surface.fill(self.settings.bg_color)
        self.board = Board2(self.display, self.surface)

        # The player here will be player 1
        self.player1 = Player()
        self.player2 = Player()

        self.turn = "player 1"

        # The Play button
        self.play_button = Buttons("Play", self.settings.game_button_font,
                                   250, 525, self.surface)
        # The Skip button
        self.skip_button = Buttons("Skip", self.settings.game_button_font,
                                   450, 525, self.surface)

    def start_game(self):
        self.deal()
        # self.update(p=False, o=False)

    # Enter name method
    def enter_name(self):
        entered_name1 = False
        entered_name2 = False
        player1_name = ""
        player2_name = ""

        while not entered_name1 or not entered_name2:

            font = self.settings.game_mode_font

            self.surface.fill(self.settings.bg_color)
            pygame.display.flip()

            string_size = 0

            if not entered_name1:
                string = "Enter Player 1 name: " + player1_name
                title = font.render(string, True, (255, 255, 255))
                title_width = font.size(string)

                string_size = title_width[0]

                self.surface.blit(title, (500 - title_width[0]/2, 200 - title_width[1]/2))

            elif entered_name1 and not entered_name2:
                string = "Enter Player 2 name: " + player2_name
                title = font.render(string, True, (255, 255, 255))
                title_width = font.size(string)

                string_size = title_width[0]

                self.surface.blit(title, (500 - title_width[0]/2, 200 - title_width[1]/2))

            self.display.blit(self.surface, (0, 0))
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if not entered_name1 and player1_name != "":
                            entered_name1 = True
                        elif not entered_name2 and player2_name != "":
                            entered_name2 = True
                    elif event.key == pygame.K_BACKSPACE:
                        if not entered_name1 and player1_name != "":
                            player1_name = player1_name[:-1]
                        elif not entered_name2 and player2_name != "":
                            player2_name = player2_name[:-1]
                    else:
                        if not entered_name1 and not font.size(event.unicode)[0] + string_size >= 1000:
                            player1_name += event.unicode
                        elif entered_name1 and not entered_name2 \
                                and not font.size(event.unicode)[0] + string_size >= 1000:
                            player2_name += event.unicode

                if entered_name2 and entered_name1:
                    break

            pygame.display.flip()

        self.player1.enter_name(player1_name)
        self.player2.enter_name(player2_name)

        self.clear()

    # Dealing The Card
    def deal(self):
        self.board.move_to_shuffle_pos(game_update=False)
        self.board.deal(self.turn)

    # Selecting a card/un-selecting cards, and or board buttons
    def select(self, mouse_x, mouse_y):
        return self.board.choose_card(mouse_x, mouse_y, self.turn)
        # self.update()

    # Updating the game
    # Draw the board
    # Draw the player's .display.flip()names
    # Draw the buttons
    def update(self, s=True, o=True, c=True, d=True, p=True):
        self.board.draw_board(shuffle=s, opponent=o, current=c, discard=d, player=p)

    def clear(self):
        self.surface.fill(self.settings.bg_color)

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

    def get_turn(self):
        return self.turn
