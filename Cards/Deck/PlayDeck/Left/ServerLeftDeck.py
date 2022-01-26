from Cards.Deck.PlayDeck.ServerSideDeck import ServerSideDeck


def update_rect(rect, x, y, width, height):
    return rect.update(x, y, width, height)


class ServerLeftDeck(ServerSideDeck):
    def __init__(self, x, y, chosen_x, width, collide_point):
        super().__init__(x, y, chosen_x, width, collide_point)

    def move_deck(self):
        num_cards = len(self.deck)
        starting = max((self.length + self.y) - (num_cards * self.card_width), self.y)

        if num_cards == 0 or num_cards == 1:
            self.card_pos = self.card_width
        else:
            self.card_pos = min(self.card_width,
                                round((self.length - self.card_width) / (num_cards - 1)))

        update_rect(self.collide_point, self.x, self.y,
                    self.card_height, min((num_cards * self.card_width), self.length))

        for i in range(len(self.deck)):
            x = self.deck[i]

            if x.cur_pos() == (self.settings.shuffle_x, self.settings.shuffle_y):
                x.rotate(270)

            if not x.get_chosen():
                # We draw the background, then draw the previous cards, then proceed.
                if self.was_chosen_deck.__contains__(x):
                    self.was_chosen_deck.remove(x)

                x.update_vis(True)
                if x.cur_pos()[0] == self.x or x.cur_pos()[0] == self.chosen_x \
                        or self.was_drag_card.__contains__(x):
                    x.move(self.x, starting)
                else:
                    x.move(self.x, starting)

                if i != len(self.deck) - 1:
                    if not self.deck[i+1].get_chosen():
                        x.update_card_block_area(self.x, starting + self.card_pos,
                                                 self.card_height, self.card_width - self.card_pos)
                    else:
                        x.update_card_block_area(self.x + self.card_height/2, starting + self.card_pos,
                                                 self.card_height/2, self.card_width - self.card_pos)
                else:
                    x.update_card_block_area(self.x, starting + self.card_pos, 0, 0)

            # Do this portion
            else:
                if self.to_be_chosen_cards.__contains__(x):
                    self.to_be_chosen_cards.remove(x)

                x.move(self.chosen_x, starting)

                original_x, original_y = x.cur_pos()

                if i != len(self.deck) - 1:
                    if not self.deck[i+1].get_chosen():
                        x.update_card_block_area(self.x + self.card_height/2,
                                                 original_y + self.card_pos,
                                                 self.chosen_x - self.x,
                                                 self.card_width - self.card_pos)
                    else:
                        x.update_card_block_area(self.chosen_x,
                                                 original_y + self.card_pos,
                                                 self.card_height,
                                                 self.card_width - self.card_pos)
                else:
                    x.update_card_block_area(self.y, original_x + self.card_pos, 0, 0)

            starting += self.card_pos
            if self.was_drag_card.__contains__(x):
                self.was_drag_card.remove(x)

    def handle_selected(self, mouse_x, mouse_y, dragging):
        i = len(self.deck) - 1
        while i >= 0:
            card = self.deck[i]
            if card.handle_selected(mouse_x, mouse_y):
                if dragging:
                    self.drag_card.append(card)
                    self.drag_card_original_index = i
                    self.deck.remove(card)
                    card_x, card_y = card.cur_pos()
                    self.mouse_x_offset = card_x - mouse_x
                    self.mouse_y_offset = card_y - mouse_y

                    return "left"
                elif card.get_chosen():
                    self.move_to_deck(card)
                    card.change_chosen(False)
                    self.was_chosen_deck.append(card)
                    return "left"
                else:
                    self.move_to_chosen(card)
                    card.change_chosen(True)
                    self.to_be_chosen_cards.append(card)
                    return "left"
            i -= 1

        if dragging and len(self.drag_card) == 0:
            return "Not Selected left"
