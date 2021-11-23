import pygame


class Cards:

    def __init__(self, win, value, suit, front_image, back_image):

        # The screen
        self.screen = win
        # Value of the card
        self.value = value
        # Suit of the card
        self.suit = suit
        # Front image of the card
        self.front_image = pygame.load(front_image)
        # Back image of the card
        self.back_image = pygame.load(back_image)

        # We will default the size of the card to be 100, 150. We will be able
        # to scale it when dealing.
        self.front_image = pygame.transform.scale(self.front_image, (100, 150))
        self.back_image = pygame.transform.scale(self.back_image, (100, 150))

        # If the user chose the card
        self.chosen = False
        # Opponent card or User card
        # We will make it default to true, so all cards will be dealt
        # face up
        self.front = True

        # Card Location
        self.x = -200
        self.y = -200

        self.rect_card = pygame.Rect(self.x, self.y, 100, 150)

    # Move the card to a different location
    # If we are moving the card to the shuffle position, we will make it appear
    # instantly. If shuffle is true, then we are moving it to the shuffle
    # position. If it is false, we are dealing, playing, which will have a smooth position.
    # We have to move the image and the rectangle at the same time.
    def move(self, x, y, shuffle):
        x_distance = x - self.x
        y_distance = y - self.y

        x_direction = "positive" if (x_distance > 0) else "negative"
        y_direction = "positive" if (y_distance > 0) else "negative"

        if x_direction == "negative":
            x_distance *= -1
        if y_direction == "negative":
            y_distance *= -1

        if x_distance != 0 and y_distance != 0:
            slope = y_distance/x_distance
        else:
            slope = 0

        if not shuffle:
            while x_distance != 0 or y_distance != 0:
                if x_distance == 0:
                    if y_direction == "negative":
                        self.y += -5
                    else:
                        self.y += -5

                    self.draw(self.front)
                    pygame.display.update()
                elif y_distance == 0:
                    if x_direction == "negative":
                        self.x += -5
                    else:
                        self.x += 5

                    self.draw(self.front)
                    pygame.display.update()
                else:
                    if x_direction == "negative":
                        self.x += -1
                    else:
                        self.x += 1

                    if y_direction == "positive":
                        self.y += -1 * slope
                    else:
                        self.y += slope

                    self.draw(self.front)
                    pygame.display.update()
        else:
            self.x = x
            self.y = y

            self.draw(self.front)
            pygame.display.update()

    def draw(self, front):
        if self.front and front:
            self.screen.blit(self.front_image, (self.x, self.y))
            self.rect_card.move(self.x, self.y)
        else:
            self.screen.blit(self.back_image, (self.x, self.y))
            self.rect_card.move(self.x, self.y)

    # Method to update the visibility of the card
    def update_vis(self, boolean):
        self.front = boolean
