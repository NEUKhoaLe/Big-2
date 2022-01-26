import pygame


class ServerButtons:
    def __init__(self, x, y, width, height):
        self.button = pygame.Rect(x, y, width, height)

    def collide_point(self, x, y):
        return self.button.collidepoint((x, y))
