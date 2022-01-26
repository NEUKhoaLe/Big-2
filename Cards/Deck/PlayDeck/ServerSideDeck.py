from Cards.ServerCard import ServerCard
from Utils.ServerSettings import ServerSettings


class ServerSideDeck:
    def __init__(self, x, y, chosen_x, length, collide_point):
        self.deck = []

        self.x = x
        self.y = y
        self.card_width = 100
        self.card_height = 150

        self.length = length
        self.collide_point = collide_point

        self.chosen_deck = []

        self.was_chosen_deck = []
        self.to_be_chosen_cards = []

        self.drag_card = []
        self.was_drag_card = []
        self.drag_card_original_index = -1
        self.mouse_x_offset = -1
        self.mouse_y_offset = -1

        self.card_mid_point_y = self.y - self.card_height/2

        self.card_pos = -1

        self.chosen_x = chosen_x
        self.settings = ServerSettings()

    def move_deck(self):
        pass

    def add_card(self, cards):
        if isinstance(cards, list):
            for card in cards:
                self.deck.append(card)
        else:
            self.deck.append(cards)

    def remove_card(self, cards):
        if isinstance(cards, list):
            for card in cards:
                self.deck.remove(card)
        elif cards == "last":
            return self.deck.pop(len(self.deck) - 1)
        elif cards == "first":
            return self.deck.pop(0)
        elif isinstance(cards, int):
            return self.deck.pop(cards)
        elif isinstance(cards, ServerCard):
            return self.deck.remove(cards)

    def transfer_all_cards_to_deck(self, deck):
        self.deck = deck.copy()

    def get_length(self):
        return len(self.deck)

    def handle_selected(self, mouse_x, mouse_y, dragging):
        pass

    def card_change_in_play(self, index, boolean):
        pass

    def draw_deck(self, move_from_shuffle, game_update=False, draw=True):
        pass

    def change_pos(self, x, y):
        self.x = x
        self.y = y

    def reset(self):
        pass

    def shuffle_deck(self):
        pass

    def get_deck(self):
        return self.deck.copy()

    def flip_vis(self, boolean):
        for card in self.deck:
            card.update_vis(boolean)

    def select_deck(self, mouse_x, mouse_y):
        general_deck = self.collide_point.collidepoint((mouse_x, mouse_y))
        collide = False

        for card in self.deck:
            collide = collide or card.handle_selected(mouse_x, mouse_y)

        return collide or general_deck

    def undrag(self, mouse_x, mouse_y):
        i = len(self.deck) - 1
        successful = False
        self.was_drag_card.append(self.drag_card[0])

        while i >= 0:
            card = self.deck[i]
            if card.handle_selected(mouse_x, mouse_y) and not card.equals(self.drag_card[0]):
                self.deck.insert(min(i+1, len(self.deck)), self.drag_card.pop())
                successful = True
                break

            i -= 1

        if not successful:
            self.deck.insert(self.drag_card_original_index, self.drag_card.pop())

        self.drag_card_original_index = -1
        self.mouse_y_offset = -1
        self.mouse_x_offset = -1
        self.drag_card = []

    def move_to_mouse(self, mouse_x, mouse_y):
        new_pos_x = mouse_x + self.mouse_x_offset
        new_pos_y = mouse_y + self.mouse_y_offset

        self.drag_card[0].move(new_pos_x, new_pos_y)

    def move_to_chosen(self, card):
        self.chosen_deck.append(card)

    def move_to_deck(self, card):
        self.chosen_deck.remove(card)

    def get_pos(self):
        return self.x, self.y
