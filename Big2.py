import pygame
import sys
from Utils.Settings import Settings
from Utils.Buttons import Buttons
from Game.Game2 import Game2


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

        self.screen.blit(title, (500 - title_width[0]/2, 200 - title_width[1]/2))

        self.solo_button.draw_button()
        self.multi_button.draw_button()
        self.rules_button.draw_button()

    # Function that handles all the mouse left click action
    def menu_mouse_action(self):
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
            self.easy_difficulty()
        elif self.hard_difficulty_button.collide_point(mouseX, mouseY):
            self.hard_difficulty()

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
        while True:
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

    # The main function that handles the pygame events on the Single Player Screen
    def single_player(self):
        """Start the main loop for the game."""
        while True:
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
        while True:
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
                        self.menu_mouse_action()
                        if self.back:
                            self.back = False
                            return

            pygame.display.flip()

    def four_player_single_mode(self):
        while True:
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
                        self.menu_mouse_action()
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
    def easy_difficulty(self):
        while True:
            self.reset_drawn_stat_rect()
            self.clock.tick(self.settings.FPS)

            self.screen.fill(self.settings.bg_color)

            self.draw_back_button()

            self.game = Game2(self.screen)

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

    def hard_difficulty(self):
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

    ###################################################################################################################
    #                                                                                                                 #
    #                                                Multiplayer Section                                              #
    #                                                                                                                 #
    ###################################################################################################################

    # The main function that handles the pygame events on the Multi Player Screen
    def multi_player(self):
        """The screen for multiplayer set up"""
        while True:
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

    # Four player online mode main method
    def four_player_online_mode(self):
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


# The statement that runs the main program
if __name__ == '__main__':
    # Make a game instance, and run the game.
    big2 = Big2()
    big2.main_menu()
