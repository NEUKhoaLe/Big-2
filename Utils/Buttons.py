import pygame
from Utils.Settings import Settings


class Buttons:

    # X and Y are location of the button. The class itself will center the word.
    def __init__(self, word, font, x, y, screen):
        self.color = (255, 255, 255)
        self.word = word
        self.font = font
        self.screen = screen
        self.settings = Settings()
        self.x = x
        self.y = y
        self.drawn = False

        self.width = font.size(word)
        self.button = pygame.Rect(self.x - self.width[0]/2 - 5, self.y - self.width[1]/2 - 5,
                                  self.width[0] + 10, self.width[1] + 10)

    def draw_button(self):
        render = self.font.render(self.word, True, (255, 255, 255))
        pygame.draw.rect(self.screen, self.settings.main_menu_button_color, self.button)
        self.screen.blit(render, (self.x - self.width[0]/2, self.y - self.width[1]/2))
        self.drawn = True

    def collide_point(self, x, y):
        return self.button.collidepoint((x, y)) and self.drawn

    def update_drawn(self, boolean):
        self.drawn = boolean
