import pygame.font
pygame.font.init()


class Settings:

    def __init__(self):
        self.screen_width = 1000
        self.screen_height = 1000
        self.bg_color = (50, 168, 105)
        self.main_menu_button_color = (50, 111, 168)

        self.big2_font = pygame.font.SysFont('jetsbrainsmono.ttf', 96)
        self.button_font = pygame.font.SysFont('jetsbrainsmono.ttf', 48)
        self.back_font = pygame.font.SysFont('jetsbrainsmono.ttf', 18)
        self.game_mode_font = pygame.font.SysFont('jetsbrainsmono.ttf', 64)
        self.bot_difficulty_font = pygame.font.SysFont('jetsbrainsmono.ttf', 64)
        self.game_button_font = pygame.font.SysFont('jetsbrainsmono.ttf', 36)
        self.player_name_font = pygame.font.SysFont('jetsbrainsmono.ttf', 50)

        self.player_deck_2_x = 50
        self.opposite_deck_2_x = 50
        self.player_y = 775
        self.opposite_y = 75
        self.player_chosen_y = 700
        self.opposite_chosen_y = 150
        self.play_deck_width_2 = 900

        self.current_deck_2_x = 100
        self.current_deck_y = 425
        self.current_deck_width_2 = 900

        self.discard_deck_x_2 = 450
        self.discard_deck_y_2 = 250

        self.player_name_x = 500
        self.player_name_y = 963

        self.opposite_name_x = 500
        self.opposite_name_y = 37

        self.play_button_x = 802
        self.play_button_y = 963
        self.skip_button_x = 903
        self.skip_button_y = 963

        self.shuffle_x = 450
        self.shuffle_y = 425

        self.player_deck_4_x = 250
        self.opposite_deck_4_x = 250
        self.left_deck_4_x = 75
        self.right_deck_4_x = 775
        self.player_deck_4_y = 775
        self.opposite_deck_4_y = 75
        self.left_deck_4_y = 250
        self.right_deck_4_y = 250

        self.player_chosen_4_y = 700
        self.opposite_chosen_4_y = 150
        self.left_chosen_4_x = 150
        self.right_chosen_4_x = 700

        self.play_deck_width_4 = 500
        self.current_deck_width_4 = 500

        self.current_deck_4_x = 250
        self.current_deck_4_y = 425

        self.discard_deck_x_4 = 750
        self.discard_deck_y_4 = 50

        self.left_name_x = 37
        self.left_name_y = 500
        self.right_name_x = 963
        self.right_name_y = 500

        self.FPS = 240
