from Board.AbstractBoard import AbstractBoard


def update_rect(rect, x, y, width, height):
    return rect.update(x, y, width, height)


class Board2(AbstractBoard):
    def __init__(self, screen):
        super().__init__(screen)

        self.opponent_deck_x = 50
        self.opponent_deck_y = 75

        self.player_deck_x = 50
        self.player_deck_y = 675

        self.play_deck_width = 800

        self.current_play_pile_x = 50
        self.current_play_pile_y = 425

        self.discard_deck_pile_x = 750
        self.discard_deck_pile_y = 50

        self.deck = self.create_deck()

    # Method to draw a given deck given a deck type
    # If it is a shuffle deck: we will draw only the top back
    # of the card
    # If it is the opponent's deck, then we will draw each card
    # moving to its place, reversed 180 degrees
    # If it is discard, we also only draw the top of the deck
    # card back
    # If it is the current play pile, we draw the card front
    # If it is in the chosen pile, we draw the card moving up
    # half its length
    def draw_deck(self, deck_type):
        if deck_type == "shuffle":
            self.move_to_shuffle_pos()
            self.deck[0].draw(False)
        elif deck_type == "opponent":
            num_cards = len(self.opponent_deck)
            starting = (self.play_deck_width + self.opponent_deck_x) - (num_cards * self.card_width)
            starting = starting / 2
            card_pos = min(self.card_width,
                           round((self.play_deck_width - self.card_width) / (num_cards - 1)))

            update_rect(self.opponent_deck_collide_point, self.opponent_deck_x, self.opponent_deck_y,
                        (num_cards * self.card_width), self.card_height)

            for x in self.opponent_deck:
                if not x.get_chosen():
                    x.update_vis(False)
                    if x.cur_pos() == (self.deck_x, self.deck_y):
                        x.rotate(180)
                    x.move(starting, self.opponent_deck_y, False)
                    x.update_card_block_area(starting + card_pos, self.card_height,
                                             self.card_width - card_pos, self.card_height)
                    x.draw()

                starting += card_pos
        elif deck_type == "current":
            num_cards = len(self.current_play_pile)
            starting = (self.play_deck_width + self.current_play_pile_x) - (num_cards * self.card_width)
            starting = starting / 2

            for x in self.current_play_pile:
                x.update_vis(True)
                x.move(starting, self.current_play_pile_y, False)
                x.draw()

                starting += x.get_width()
        elif deck_type == "discard":
            for x in self.current_play_pile:
                x.move(self.discard_deck_pile_x, self.discard_deck_pile_y, False)
                x.update_vis(False)

            card = self.discard_deck_pile[len(self.discard_deck_pile) - 1]
            card.draw()
        elif deck_type == "player":
            num_cards = len(self.player_deck)
            starting = (self.play_deck_width + self.player_deck_x) - (num_cards * self.card_width)
            starting = starting / 2
            card_pos = min(self.card_width,
                           round((self.play_deck_width - self.card_width) / (num_cards - 1)))

            update_rect(self.player_deck_collide_point, self.player_deck_x, self.player_deck_y,
                        (num_cards * self.card_width), self.card_height)

            for x in self.player_deck:
                if not x.get_chosen():
                    x.update_vis(True)
                    x.move(starting, self.player_deck, False)
                    x.update_card_block_area(starting + card_pos, self.card_height,
                                             self.card_width - card_pos, self.card_height)
                    x.draw()

                starting += x.get_width()
        elif deck_type == "player-chosen":
            for card in self.player_chosen:
                x, y = card.cur_pos()
                card.move(x, self.player_chosen_height)

                num_cards = len(self.player_deck)
                card_pos = min(self.card_width,
                               round((self.play_deck_width - self.card_width) / (num_cards - 1)))
                original_x, original_y = card.cur_pos()
                card.update_card_block_area(original_x + card_pos,
                                            self.player_deck_y,
                                            self.card_width - card_pos,
                                            self.player_deck_y - self.player_chosen_height)
                card.draw()
        elif deck_type == "opponent-chosen":
            for card in self.opponent_chosen:
                x, y = card.cur_pos()
                card.move(x, self.opponent_chosen_height)
                num_cards = len(self.opponent_deck)
                card_pos = min(self.card_width,
                               round((self.play_deck_width - self.card_width) / (num_cards - 1)))
                original_x, original_y = card.cur_pos()
                card.update_card_block_area(original_x + card_pos,
                                            self.opponent_deck_y,
                                            self.card_width - card_pos,
                                            self.opponent_chosen_height - self.opponent_deck_y)
                card.draw()

    # Method to deal the shuffled card.
    # takes in the winner of the last game.
    # deals in counter clock-wise
    # Must implement the move.
    def deal(self, last_winner):
        counter = 0
        if last_winner == "player 1":
            for card in self.deck:
                card.change_in_play(True)
                if counter % 2 == 0:
                    self.player_deck.append(card)
                    self.deck.remove(card)
                    self.draw_deck("player")
                else:
                    card.update_vis(False)
                    self.opponent_deck.append(card)
                    self.deck.remove(card)
                    self.draw_deck("opponent")
                counter += 1
        else:
            for card in self.deck:
                card.change_in_play(True)
                if counter % 2 == 1:
                    self.player_deck.append(card)
                    self.deck.remove(card)
                    self.draw_deck("player")
                else:
                    card.update_vis(False)
                    self.opponent_deck.append(card)
                    self.deck.remove(card)
                    self.draw_deck("opponent")
                counter += 1

    # Method to move card from play pile to chosen pile
    def move_play_to_chosen(self, card, deck_type):
        if deck_type == "player":
            card.change_chosen(True)
            self.player_chosen.append(card)

            self.draw_deck("player-chosen")
            self.draw_deck("player")
        elif deck_type == "opponent":
            card.change_chosen(True)
            self.opponent_chosen.append(card)

            self.draw_deck("opponent-chosen")
            self.draw_deck("opponent")

    def move_chosen_to_play(self, card, deck_type):
        if deck_type == "player":
            card.change_chosen(False)
            self.player_chosen.remove(card)

            self.draw_deck("player-chosen")
            self.draw_deck("player")
        elif deck_type == "opponent":
            card.change_chosen(False)
            self.opponent_chosen.remove(card)

            self.draw_deck("opponent-chosen")
            self.draw_deck("opponent")

    # Method to move card from pile to the play pile
    def move_chosen_to_current(self, pile_from, cards):
        if pile_from == "player":
            for card in cards:
                card.change_in_play(False)
                self.current_play_pile.append(card)
                self.player_chosen.remove(card)
                self.player_deck.remove(card)
                self.draw_deck("current")
                self.draw_deck("player")
        elif pile_from == "opponent":
            for card in cards:
                card.change_in_play(False)
                self.current_play_pile.append(card)
                self.opponent_chosen.remove(card)
                self.opponent_deck.remove(card)
                self.draw_deck("current")
                self.draw_deck("opponent")

    # Method to flip the visibility.
    def flip_vis(self, deck_type, boolean):
        if deck_type == "opponent":
            for card in self.opponent_deck:
                card.udate_vis(boolean)
        elif deck_type == "player":
            for card in self.player_deck:
                card.update_vis(boolean)

    # Handle collision. Choosing a card. Passes in x and y position of mouse. First find which deck was chosen
    # and then go through every card in that deck to find the card. Move that card to the chosen
    # If a chosen card is selected, then it is "unchosen" i.e. removed from the chosen pile
    def choose_card(self, mouse_x, mouse_y, cur_player):
        if self.opponent_deck_collide_point.collidepoint(mouse_x, mouse_y):
            deck_type = "opponent"

            if cur_player == deck_type:
                for card in self.opponent_deck:
                    if card.handle_selected():
                        if card.get_chosen():
                            self.move_chosen_to_play(card, deck_type)
                        else:
                            self.move_play_to_chosen(card, deck_type)
        elif self.player_deck_collide_point.collidepoint(mouse_x, mouse_y):
            deck_type = "player"

            if cur_player == deck_type:
                for card in self.player_deck:
                    if card.get_chosen():
                        self.move_chosen_to_play(card, deck_type)
                    else:
                        self.move_play_to_chosen(card, deck_type)
        else:
            for card in self.opponent_chosen:
                if card.handle_selected(mouse_x, mouse_y) and cur_player == "opponent":
                    if card.get_chosen():
                        self.move_chosen_to_play(card, "opponent")
                    else:
                        self.move_play_to_chosen(card, "opponent")

                    return
            for card in self.player_chosen:
                if card.handle_selected(mouse_x, mouse_y) and cur_player == "player":
                    if card.get_chosen():
                        self.move_chosen_to_play(card, "player")
                    else:
                        self.move_play_to_chosen(card, "player")

                    return

            if cur_player == "player":
                for card in self.player_chosen:
                    self.move_chosen_to_play(card, "player")
            elif cur_player == "opponent":
                for card in self.opponent_chosen:
                    self.move_chosen_to_play(card, "opponent")
