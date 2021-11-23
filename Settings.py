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

        self.FPS = 60
