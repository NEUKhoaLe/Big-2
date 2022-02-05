import socket
import pickle

import pygame

from Game.Player2.Game2Online import Game2Online
from Utils.Settings import Settings


class NetworkClient:
    def __init__(self, display):
        self.display = display
        self.settings = Settings()
        self.dragging = False
        self.client_name = None
        self.game = None

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.1.241"
        self.port = 5555
        self.addr = (self.server, self.port)

        self.player_number = self.connect()
        self.play()

    def setup(self):
        temp = pygame.Surface((self.settings.screen_width, self.settings.screen_height))
        self.display.blit(temp, (0, 0))
        self.client_name = self.enter_name(temp)

    def get_player(self):
        return self.player_number

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except:
            pass

    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return pickle.loads(self.client.recv(2048 * 2))
        except socket.error as e:
            print(e)

    def play(self):
        self.setup()

        title_font = self.settings.big2_font
        title = title_font.render("Waiting for other players", True, (255, 255, 255))
        title_width = title_font.size("Waiting for other players")

        self.display.blit(title, (500 - title_width[0] / 2, 500 - title_width[1] / 2))
        # Get the game to initialize and add the player name into the server's game client
        reply = self.send("get")

        # Initialize the client-side game.
        self.game = Game2Online(self.display, self.player_number)
        # Initial reconciliation with server.
        self.game.reconcile(reply, self.player_number)

        # Creating the player.
        if self.player_number == 1:
            self.game.create_player(self.client_name, None)
        elif self.player_number == 2:
            self.game.create_player(None, self.client_name)

        # After changing the name in the client side, we send the instruction to the
        # Server. The below are the server instructions so far:
        # "click <x y>" - selecting card, playing, skipping, choosing a card
        # "name <name>"
        # "swap index index"

        # Dragging will be a client side action. Only when we release AND does a swap movement
        # then we will update the server.
        # after sending the instruction, we reconcile.
        # In this reconciliation process, if everything is the same, then nothing happens
        # If everything is not, we will draw the server's game state, as the server is
        # the authority here.

        # We will send a tuple to the client, which is [game_object, player_int]
        # If the player_int doesn't match with the client player number, then there
        # is no need to reconcile.
        self.game.reconcile(self.send("name " + self.client_name), self.player_number)

        # While the server is not ready, we print a screen that says "Waiting for another player"
        # No matter what we do, we will always reconcile with the server at the end

        while not self.game.get_ready():
            self.display.fill(self.settings.bg_color)
            self.display.blit(title, (500 - title_width[0] / 2, 500 - title_width[1] / 2))

            pygame.display.flip()

            self.game.reconcile(self.send("get"), self.player_number)

        run = True

        self.game.reconcile(self.send("get"), self.player_number)
        self.game.start_game()
        self.dragging = False

        self.game.update()

        while run:
            self.reset_drawn_stat_rect()
            self.clock.tick(self.settings.FPS)

            self.screen.fill(self.settings.bg_color)

            self.draw_back_button()

            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.menu_mouse_action()
                        if self.back:
                            self.back = False
                            return

            pygame.display.flip()

    # Enter name method
    def enter_name(self, surface):
        entered_name1 = False
        player1_name = ""

        while not entered_name1:

            font = self.settings.game_mode_font

            surface.fill(self.settings.bg_color)
            pygame.display.flip()

            string_size = 0

            if not entered_name1:
                string = "Enter Player 1 name: " + player1_name
                title = font.render(string, True, (255, 255, 255))
                title_width = font.size(string)

                string_size = title_width[0]

                surface.blit(title, (500 - title_width[0]/2, 200 - title_width[1]/2))

            self.display.blit(surface, (0, 0))
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if not entered_name1 and player1_name != "":
                            entered_name1 = True
                    elif event.key == pygame.K_BACKSPACE:
                        if not entered_name1 and player1_name != "":
                            player1_name = player1_name[:-1]
                    else:
                        if not entered_name1 and not font.size(event.unicode)[0] + string_size >= 1000:
                            player1_name += event.unicode
                if entered_name1:
                    break

            pygame.display.flip()

        return player1_name
