import pygame


class Player:
    def __init__(self, name=""):
        self.name = name
        self.score = 0

    def enter_name(self, name):
        self.name = name

    def enter_score(self, score):
        self.score = score
