import pygame.font


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
        self.opponent_deck_2_x = 50
        self.player_y = 775
        self.opponent_y = 75
        self.player_chosen_y = 700
        self.opponent_chosen_y = 150
        self.play_deck_width_2 = 900

        self.current_deck_2_x = 100
        self.current_deck_y = 425
        self.current_deck_width_2 = 900

        self.discard_deck_x_2 = 750
        self.discard_deck_y_2 = 50

        self.shuffle_x = 450
        self.shuffle_y = 425

        self.FPS = 240
