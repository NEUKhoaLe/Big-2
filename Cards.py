import pygame


class Cards:

    def __init__(self, value, suit, front_image, back_image):

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
        self.is_player = True

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
        pass

    # This method is used to
    def update(self):
        pass

