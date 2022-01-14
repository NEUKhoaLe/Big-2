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

    def enter_deck(self, deck):
        self.deck = deck

    def draw_deck(self, draw_from_shuffle, game_update=False):
        self.deck.draw_deck(draw_from_shuffle, game_update)

    def add_card(self, card):
        self.deck.add_card(card)

    def flip_vis(self, boolean):
        self.deck.flip_vis(boolean)

    def select_deck(self, mouse_x, mouse_y):
        return self.deck.select_deck(mouse_x, mouse_y)

    def handle_selected(self, mouse_x, mouse_y, dragging):
        return self.deck.handle_selected(mouse_x, mouse_y, dragging)

    def get_pos(self):
        return self.deck.get_pos()

    def change_pos(self, x, y):
        self.deck.change_pos(x, y)

    def get_chosen_deck(self):
        return self.deck.get_chosen()

    def undrag(self, mouse_x, mouse_y):
        self.deck.undrag(mouse_x, mouse_y)

    def move_to_mouse(self, mouse_x, mouse_y):
        self.deck.move_to_mouse(mouse_x, mouse_y)

    def update_draw(self):
        self.deck.update_draw()
