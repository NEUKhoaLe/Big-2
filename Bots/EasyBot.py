import pygame

from Game.Player import Player
from Utils.Settings import Settings


class EasyBot:
    def __init__(self, surface, name, deck):
        self.board = None
        self.deck = deck
        self.surface = surface
        self.name = Player(self.surface, player_type=self.deck)
        self.name.enter_name(name)
        self.score = 0
        self.settings = Settings()

    def add_board(self, board):
        self.board = board

    def draw_name(self):
        self.name.draw_name()

    def enter_score(self, score):
        self.name.enter_score(score)

    def get_score(self):
        return self.name.get_score()

    def enter_surface(self, surface):
        self.name.enter_surface(surface)
