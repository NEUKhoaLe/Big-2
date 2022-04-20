import pygame

from Utils.Settings import Settings


class Message:
    def __init__(self, surface, display):
        self.message = ""
        self.settings = Settings()
        self.surface = surface
        self.display = display

    def draw_message(self, message):
        background = pygame.Surface((450, 30))
        background.fill(self.settings.bg_color)
        self.surface.blit(background, (self.settings.message_x, self.settings.message_y - 30 / 2))

        self.message = message

        font = self.settings.message_font
        message_rendered = font.render(self.message, True, (255, 255, 255))
        message_size = font.size(self.message)

        self.surface.blit(message_rendered, (self.settings.message_x,
                                             self.settings.message_y - message_size[1] / 2))

        pygame.display.flip()
