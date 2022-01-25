import pygame

from Utils.Settings import Settings


class Player:
    def __init__(self, surface, player_type="", name=""):
        self.name = name
        self.deck = None
        self.score = 0
        self.surface = surface
        self.player_type = player_type
        self.settings = Settings()

    def get_name(self):
        return self.name

    def enter_name(self, name):
        self.name = name

    def enter_score(self, score):
        self.score = score

    def draw_name(self):
        font = pygame.font.SysFont('jetsbrainsmono.ttf', 36)
        name_rendered = font.render(self.name + " (" + str(self.score) + ")", True, (255, 255, 255))
        name_width = font.size(self.name + " (" + str(self.score) + ")")

        if self.player_type == "player":
            self.surface.blit(name_rendered, (self.settings.player_name_x - name_width[0]/2,
                                              self.settings.player_name_y - name_width[1]/2))
        elif self.player_type == "opposite":
            self.surface.blit(name_rendered, (self.settings.opposite_name_x - name_width[0]/2,
                                              self.settings.opposite_name_y - name_width[1]/2))
        elif self.player_type == "left":
            pass
        elif self.player_type == "right":
            pass
