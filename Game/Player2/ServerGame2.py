from Board.Board2.ServerBoard2 import ServerBoard2
from Game.ServerPlayer import ServerPlayer
from Utils.ServerButtons import ServerButtons
from Utils.ServerSettings import ServerSettings


class ServerGame2:
    def __init__(self, game_id):
        self.settings = ServerSettings()

        self.turn = "player"
        self.have_selected_card_drag = False

        self.board = None

        self.game_id = game_id

        self.player1 = None
        self.player2 = None

        self.server_ready = False

        self.play_button = ServerButtons(758.0, 945.5, 88, 35)
        self.skip_button = ServerButtons(856.5, 945.5, 93, 35)

    def start_game(self):
        self.deal()

    def set_ready(self, boolean):
        self.server_ready = boolean

    def create_player(self, player1_name, player2):
        if type(player1_name) is str:
            self.player1 = ServerPlayer(player_type="player", name=player1_name)
        else:
            self.player1 = player1_name

        if type(player2) is str:
            self.player2 = ServerPlayer(player_type="opposite", name=player2)
            self.player2.enter_name(player2)
        elif not None:
            self.player2 = player2

        self.board = ServerBoard2()

    # If player number 2, player_deck = 2, opposite_deck = 1
    def swap_decks(self, player_number):
        if player_number == 1:
            order = [1, 2]
        else:
            order = [2, 1]

        self.board.rotate_deck(order)

    def get_player(self, player_number):
        if player_number == 1:
            return self.player1.copy()
        elif player_number == 2:
            return self.player2.copy()

    # Dealing The Card
    def deal(self):
        self.board.move_to_shuffle_pos(game_update=False)
        self.board.deal(self.turn)

    # Selecting a card/un-selecting cards, and or board buttons
    def select(self, mouse_x, mouse_y):
        if self.play_button.collide_point(mouse_x, mouse_y):
            self.board.play(self.turn)
        elif self.skip_button.collide_point(mouse_x, mouse_y):
            self.change_turn()
        else:
            return self.board.choose_card(mouse_x, mouse_y, self.turn, False)

    def play_hand(self):
        pass

    def quit(self):
        pass

    def change_turn(self):
        if self.turn == "player":
            self.turn = "opposite"
        elif self.turn == "opposite":
            self.turn = "player"

    def change_score(self):
        pass

    def get_turn(self):
        return self.turn

    def dragging_card(self, mouse_x, mouse_y, dragging):
        if not self.have_selected_card_drag and dragging:
            answer = self.board.choose_card(mouse_x, mouse_y, self.turn, dragging)
            if answer == "Not Selected player" or answer == "Not Selected opposite":
                self.have_selected_card_drag = False
                return "nothing"
            else:
                self.have_selected_card_drag = True

        if dragging and self.have_selected_card_drag:
            self.board.move_to_mouse(mouse_x, mouse_y, self.turn)

        if not dragging:
            if self.have_selected_card_drag:
                self.board.undrag(mouse_x, mouse_y, self.turn)
                self.have_selected_card_drag = False
            else:
                return "nothing"

    def get_board(self):
        return self.board.copy()
