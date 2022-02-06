import select

import pygame
import sys

from Game.Player2.Game2Online import Game2Online
from Game.Player4.Game4Bot import Game4Bot
from Network import Network
from Utils.Settings import Settings
from Utils.Buttons import Buttons
from Game.Player2.Game2Bot import Game2Bot

"""
This is the Big 2. It will represent the client. It will speak to a server.
When a player launches the game, they will become the client.

Big 2 is the class that will communicate to the server through a network.
This game will be run through a client-server networking system.
"""


class Big2:
    """ Overall class to manage game assets and behavior."""

    def __init__(self):
        """ Initialize the game, and create game resources."""
        pygame.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Big 2")
        self.clock = pygame.time.Clock()

        main_screen_font = self.settings.button_font
        back_font = self.settings.back_font

        self.back = False

        self.game = None
        self.player_number = None

        self.dragging = None

        self.back_button = Buttons("Back", back_font, 25, 25, self.screen)
        self.solo_button = Buttons("Single Player", main_screen_font, 500, 500, self.screen)
        self.multi_button = Buttons("Multi Player", main_screen_font, 500, 550, self.screen)
        self.rules_button = Buttons("Rules", main_screen_font, 500, 600, self.screen)

        self.two_player_single_button = Buttons("Two Player", self.settings.game_mode_font, 500, 400, self.screen)
        self.four_player_single_button = Buttons("Four Player", self.settings.game_mode_font, 500, 600, self.screen)
        self.two_player_online_button = Buttons("Two Player", self.settings.game_mode_font, 500, 400, self.screen)
        self.four_player_online_button = Buttons("Four Player", self.settings.game_mode_font, 500, 600, self.screen)

        self.easy_difficulty_button = Buttons("Easy Difficulty", self.settings.bot_difficulty_font,
                                              500, 400, self.screen)
        self.hard_difficulty_button = Buttons("Hard Difficulty", self.settings.bot_difficulty_font,
                                              500, 600, self.screen)

    # Function to Draw the back button
    def draw_back_button(self):
        self.back_button.draw_button()

    # Function to Draw the two different game mode:
    #   - Two-player
    #   - Four-player
    def draw_single_game_mode_button(self):
        self.two_player_single_button.draw_button()
        self.four_player_single_button.draw_button()

    # Function for two different game mode online:
    def draw_online_game_mode_button(self):
        self.two_player_online_button.draw_button()
        self.four_player_online_button.draw_button()

    # Function to Draw the two different difficulties when playing against AI:
    def draw_bot_difficulty_button(self):
        self.easy_difficulty_button.draw_button()
        self.hard_difficulty_button.draw_button()

    # Function to Draw the rest of the main menu
    def draw_text_menu(self):
        title_font = self.settings.big2_font
        title = title_font.render("Big 2", True, (255, 255, 255))
        title_width = title_font.size("Big 2")

        self.screen.blit(title, (500 - title_width[0] / 2, 200 - title_width[1] / 2))

        self.solo_button.draw_button()
        self.multi_button.draw_button()
        self.rules_button.draw_button()

    # Function that handles all the mouse left click action
    def menu_mouse_action(self, num_player=2):
        mouseX, mouseY = pygame.mouse.get_pos()

        if self.back_button.collide_point(mouseX, mouseY):
            self.back = True
        elif self.solo_button.collide_point(mouseX, mouseY):
            self.single_player()
        elif self.multi_button.collide_point(mouseX, mouseY):
            self.multi_player()
        elif self.rules_button.collide_point(mouseX, mouseY):
            self.rules()
        elif self.two_player_single_button.collide_point(mouseX, mouseY):
            self.two_player_single_mode()
        elif self.four_player_single_button.collide_point(mouseX, mouseY):
            self.four_player_single_mode()
        elif self.two_player_online_button.collide_point(mouseX, mouseY):
            self.two_player_online_mode()
        elif self.four_player_online_button.collide_point(mouseX, mouseY):
            self.four_player_online_mode()
        elif self.easy_difficulty_button.collide_point(mouseX, mouseY):
            self.easy_difficulty(num_player)
        elif self.hard_difficulty_button.collide_point(mouseX, mouseY):
            self.hard_difficulty(num_player)

    # Function that resets all the rectangles drawn status
    def reset_drawn_stat_rect(self):
        self.back_button.update_drawn(False)
        self.solo_button.update_drawn(False)
        self.multi_button.update_drawn(False)
        self.rules_button.update_drawn(False)
        self.two_player_single_button.update_drawn(False)
        self.four_player_single_button.update_drawn(False)
        self.two_player_online_button.update_drawn(False)
        self.four_player_online_button.update_drawn(False)
        self.easy_difficulty_button.update_drawn(False)
        self.hard_difficulty_button.update_drawn(False)

    ###################################################################################################################
    #                                                                                                                 #
    #                                                 Main Menu Section                                               #
    #                                                                                                                 #
    ###################################################################################################################

    # The main function that handles the pygame events on the main menu screen
    def main_menu(self):
        """Start the main loop for the game."""
        run = True

        while run:
            self.reset_drawn_stat_rect()
            self.clock.tick(self.settings.FPS)

            self.screen.fill(self.settings.bg_color)
            self.draw_text_menu()

            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.menu_mouse_action()

            # Make the most recently drawn screen visible.
            pygame.display.flip()

    # The main function that handles the pygame events on the Rules Screen
    def rules(self):
        """The loop that displays the rules"""
        run = True

        while run:
            self.reset_drawn_stat_rect()
            self.clock.tick(self.settings.FPS)

            self.screen.fill(self.settings.bg_color)

            self.draw_back_button()

            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.menu_mouse_action()
                        if self.back:
                            self.back = False
                            return

            pygame.display.flip()

    # The main function that handles the pygame events on the Single Player Screen
    def single_player(self):
        """Start the main loop for the game."""
        run = True

        while run:
            self.reset_drawn_stat_rect()
            self.clock.tick(self.settings.FPS)

            self.screen.fill(self.settings.bg_color)

            self.draw_back_button()
            self.draw_single_game_mode_button()

            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.menu_mouse_action()
                        if self.back:
                            self.back = False
                            return

            # Make the most recently drawn screen visible
            pygame.display.flip()

    def two_player_single_mode(self):
        run = True

        while run:
            self.reset_drawn_stat_rect()
            self.clock.tick(self.settings.FPS)

            self.screen.fill(self.settings.bg_color)

            self.draw_bot_difficulty_button()
            self.draw_back_button()

            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.menu_mouse_action(2)
                        if self.back:
                            self.back = False
                            return

            pygame.display.flip()

    def four_player_single_mode(self):
        run = True

        while run:
            self.reset_drawn_stat_rect()
            self.clock.tick(self.settings.FPS)

            self.screen.fill(self.settings.bg_color)

            self.draw_bot_difficulty_button()
            self.draw_back_button()

            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.menu_mouse_action(4)
                        if self.back:
                            self.back = False
                            return

            pygame.display.flip()

    ###################################################################################################################
    #                                                                                                                 #
    #                                               Single Player Section                                             #
    #                                                                                                                 #
    ###################################################################################################################

    """
    A Game class that is the API. It stores all the methods that is required for you to run a game.
    """

    def easy_difficulty(self, num_player):
        run = True

        self.game = Game2Bot(self.screen) if num_player == 2 else Game4Bot(self.screen)
        temp = pygame.Surface((self.settings.screen_width, self.settings.screen_height))
        self.screen.blit(temp, (0, 0))
        player1_name = self.enter_name(temp)

        if num_player == 2:
            self.game.create_player(player1_name, "easy bot")
        else:
            self.game.create_player(player1_name, "easy bot", "easy bot", "easy bot")

        self.game.start_game()
        self.dragging = False

        self.game.update()

        while run:

            self.reset_drawn_stat_rect()
            self.clock.tick(self.settings.FPS)

            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if self.game.get_turn() == "player":
                            mouse_x, mouse_y = pygame.mouse.get_pos()
                            deck_selected = self.game.select(mouse_x, mouse_y)

                            if deck_selected == "player":
                                self.game.update(o=False, c=False, d=False, s=False, l=False, r=False, gu=False)
                        elif self.game.get_turn() == "opposite":
                            mouse_x, mouse_y = pygame.mouse.get_pos()
                            deck_selected = self.game.select(mouse_x, mouse_y)
                            if deck_selected == "opposite":
                                self.game.update(p=False, c=False, d=False, s=False, l=False, r=False, gu=False)
                        elif self.game.get_turn() == "left":
                            mouse_x, mouse_y = pygame.mouse.get_pos()
                            deck_selected = self.game.select(mouse_x, mouse_y)
                            if deck_selected == "left":
                                self.game.update(o=False, r=False, p=False, c=False, d=False, s=False, gu=False)
                        elif self.game.get_turn() == "right":
                            mouse_x, mouse_y = pygame.mouse.get_pos()
                            deck_selected = self.game.select(mouse_x, mouse_y)
                            if deck_selected == "right":
                                self.game.update(o=False, l=False, p=False, c=False, d=False, s=False, gu=False)
                    if event.button == 3:
                        self.dragging = True
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 3:
                        self.dragging = False
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        self.game.dragging_card(mouse_x, mouse_y, self.dragging)

                        self.game.update(gu=True)

            if self.dragging:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                self.game.dragging_card(mouse_x, mouse_y, self.dragging)

            pygame.display.flip()

    def hard_difficulty(self, num_player):
        run = True

        while run:
            self.reset_drawn_stat_rect()
            self.clock.tick(self.settings.FPS)

            self.screen.fill(self.settings.bg_color)

            self.draw_back_button()

            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.menu_mouse_action()
                        if self.back:
                            self.back = False
                            return

            pygame.display.flip()

    ###################################################################################################################
    #                                                                                                                 #
    #                                                Multiplayer Section                                              #
    #                                                                                                                 #
    ###################################################################################################################

    # The main function that handles the pygame events on the Multi Player Screen
    def multi_player(self):
        """The screen for multiplayer set up"""
        run = True

        while run:
            self.reset_drawn_stat_rect()
            self.clock.tick(self.settings.FPS)

            self.screen.fill(self.settings.bg_color)

            self.draw_back_button()
            self.draw_online_game_mode_button()

            # Watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.menu_mouse_action()
                        if self.back:
                            self.back = False
                            return

            pygame.display.flip()

    # Two player online mode main method
    def two_player_online_mode(self):
        run = False
        # Get the client's name
        temp = pygame.Surface((self.settings.screen_width, self.settings.screen_height))
        self.screen.blit(temp, (0, 0))
        client_name = self.enter_name(temp)
        self.dragging = False

        title_font = self.settings.big2_font
        title = title_font.render("Waiting for other players", True, (255, 255, 255))
        title_width = title_font.size("Waiting for other players")

        self.screen.blit(title, (500 - title_width[0] / 2, 500 - title_width[1] / 2))

        # Connect to the network, which will automatically get the player number.
        network = Network()
        # Get the player number
        self.player_number = int(network.get_player())
        # Get the game to initialize and add the player name into the server's game client
        reply = network.send("get")

        # Initialize the client-side game.
        self.game = Game2Online(self.screen, self.player_number)
        # Initial reconciliation with server.
        self.game.reconcile(reply, self.player_number)

        self.game.create_player(client_name, None)

        # After changing the name in the client side, we send the instruction to the
        # Server. The below are the server instructions so far:
        # "click <x y>" - selecting card, playing, skipping, choosing a card
        # "name <name>"
        # "swap index index"

        # Dragging will be a client side action. Only when we release AND does a swap movement
        # then we will update the server.
        # after sending the instruction, we reconcile.
        # In this reconciliation process, if everything is the same, then nothing happens
        # If everything is not, we will draw the server's game state, as the server is
        # the authority here.

        # We will send a tuple to the client, which is [game_object, player_int]
        # If the player_int doesn't match with the client player number, then there
        # is no need to reconcile.
        self.game.reconcile(network.send("name " + client_name), self.player_number)
        # While the server is not ready, we print a screen that says "Waiting for another player"
        # No matter what we do, we will always reconcile with the server at the end

        socket = network.get_socket()

        while not self.game.get_ready():
            self.screen.fill(self.settings.bg_color)
            self.screen.blit(title, (500 - title_width[0] / 2, 500 - title_width[1] / 2))

            pygame.display.flip()

            self.game.reconcile(network.send("get"), self.player_number)

        run = True
        self.dragging = False

        # Now we go into a while loop to listen for the start message
        while True:
            try:
                message = socket.recv(4096).decode()
            except:
                pass
            else:
                self.game.execute_instructions(message)
                self.game.reconcile(network.recvall(), self.player_number)
                break

        self.game.update()

        while run:
            self.reset_drawn_stat_rect()
            self.clock.tick(self.settings.FPS)

            self.screen.fill(self.settings.bg_color)

            self.draw_back_button()

            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.menu_mouse_action()
                        if self.back:
                            self.back = False
                            return

            pygame.display.flip()

    # Four player online mode main method
    def four_player_online_mode(self):

        # Get the client's name
        temp = pygame.Surface((self.settings.screen_width, self.settings.screen_height))
        self.screen.blit(temp, (0, 0))
        client_name = self.enter_name(temp)

        # Connect to the network, which will automatically get the player number.
        network = Network()
        # Get the player number
        self.player_number = str(network.get_player())
        # Get the game to initialize and add the player name into the server's game client
        self.game = network.send("get")

        # Process: Client-prediction Server Reconciliation
        # We want the client to always be the deck at the bottom. So when
        # We get the game client from the server. We switch rotate the board.
        # Do the action on the client, then rotate it back.
        # In the beginning, just to add the name, we do not have to do rotation.
        if self.player_number == 1:
            self.game.create_player(client_name, None, None, None)
        elif self.player_number == 2:
            self.game.create_player(None, client_name, None, None)
        elif self.player_number == 3:
            self.game.create_player(None, None, client_name, None)
        elif self.player_number == 4:
            self.game.create_player(None, None, None, client_name)

        # After changing the name in the client side, we send the instruction to the
        # Server. The below are the server instructions so far:
        # "click <x y>" - selecting card, playing, skipping, choosing a card
        # "name <name>"
        # "swap index index"

        # Dragging will be a client side action. Only when we release AND does a swap movement
        # then we will update the server.
        # after sending the instruction, we reconcile.
        # In this reconciliation process, if everything is the same, then nothing happens
        # If everything is not, we will draw the server's game state, as the server is
        # the authority here.
        self.game.reconcile(network.send(client_name))

        while True:
            self.reset_drawn_stat_rect()
            self.clock.tick(self.settings.FPS)

            self.screen.fill(self.settings.bg_color)

            self.draw_back_button()

            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.menu_mouse_action()
                        if self.back:
                            self.back = False
                            return

            pygame.display.flip()

    # Enter name method
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

            self.screen.blit(surface, (0, 0))
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


# The statement that runs the main program
if __name__ == '__main__':
    # Make a game instance, and run the game.
    big2 = Big2()
    big2.main_menu()
