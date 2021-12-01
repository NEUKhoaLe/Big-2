from Board.Board2 import Board2
from Game.AbstractGame import AbstractGame
from Game.Player import Player
from Utils.Buttons import Buttons
import pygame


def _keys(key):
    if key[pygame.K_RETURN]:
        return "enter"
    elif key[pygame.K_a]:
        return "a"
    elif key[pygame.K_b]:
        return "b"
    elif key == pygame.K_c:
        return "c"
    elif key == pygame.K_d:
        return "d"
    elif key == pygame.K_e:
        return "e"
    elif key == pygame.K_f:
        return "f"
    elif key == pygame.K_g:
        return "g"
    elif key == pygame.K_h:
        return "h"
    elif key == pygame.K_i:
        return "i"
    elif key == pygame.K_j:
        return "j"
    elif key == pygame.K_k:
        return "k"
    elif key == pygame.K_l:
        return "l"
    elif key == pygame.K_m:
        return "m"
    elif key == pygame.K_n:
        return "n"
    elif key == pygame.K_o:
        return "o"
    elif key == pygame.K_p:
        return "p"
    elif key == pygame.K_q:
        return "q"
    elif key == pygame.K_r:
        return "r"
    elif key == pygame.K_s:
        return "s"
    elif key == pygame.K_t:
        return "t"
    elif key == pygame.K_u:
        return "u"
    elif key == pygame.K_v:
        return "v"
    elif key == pygame.K_w:
        return "w"
    elif key == pygame.K_x:
        return "x"
    elif key == pygame.K_y:
        return "o"
    elif key == pygame.K_o:
        return "x"
    elif key == pygame.K_0:
        return "0"
    elif key == pygame.K_1:
        return "1"
    elif key == pygame.K_2:
        return "2"
    elif key == pygame.K_3:
        return "3"
    elif key == pygame.K_4:
        return "4"
    elif key == pygame.K_5:
        return "5"
    elif key == pygame.K_6:
        return "6"
    elif key == pygame.K_7:
        return "7"
    elif key == pygame.K_8:
        return "8"
    elif key == pygame.K_9:
        return "9"
    else:
        return ""


class Game2(AbstractGame):
    def __init__(self, win):

        super().__init__(win)

        self.board = Board2(self.screen)

        # The player here will be player 1
        self.player1 = Player()
        self.player2 = Player()

        self.turn = "player 1"

        # The Play button
        self.play_button = Buttons("Play", self.settings.game_button_font,
                                   250, 525, self.screen)
        # The Skip button
        self.skip_button = Buttons("Skip", self.settings.game_button_font,
                                   450, 525, self.screen)

        entered_name1 = False
        entered_name2 = False
        player1_name = ""
        player2_name = ""

        while not entered_name1 or not entered_name2:

            font = self.settings.big2_font

            self.screen.fill(self.settings.bg_color)



            if not entered_name1:
                string = "Enter Player 1 name: " + player1_name
                title = font.render(string, True, (255, 255, 255))
                title_width = font.size(string)

                self.screen.blit(title, (500 - title_width[0]/2, 200 - title_width[1]/2))

            elif entered_name1 and not entered_name2:
                string = "Enter Player 2 name: " + player2_name
                title = font.render(string, True, (255, 255, 255))
                title_width = font.size(string)

                self.screen.blit(title, (500 - title_width[0]/2, 200 - title_width[1]/2))

            pygame.display.flip()

            for event in pygame.event.get():
                keys = pygame.key.get_pressed()

                for key in keys:
                    letter = _keys(key)

                    if letter == "enter":
                        if entered_name1 != "":
                            entered_name1 = True
                        elif entered_name1 and not entered_name2:
                            if entered_name2 != "":
                                entered_name2 = True
                    else:
                        if not entered_name1:
                            player1_name += letter
                        elif entered_name1 and not entered_name2:
                            player2_name += letter

            pygame.display.flip()

        self.player1.enter_name(player1_name)
        self.player2.enter_name(player2_name)

    def start_game(self):
        self.board.deal(self.turn)

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
