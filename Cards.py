import pygame


class Cards:

    def __init__(self, value, suit, front_image, back_image):

        # Value of the card
        self.value = value
        # Suit of the card
        self.suit = suit
        # Front image of the card
        self.front_image = front_image
        # Back image of the card
        self.back_image = back_image

        # If the user chose the card
        self.chosen = False
        # Opponent card or User card
        # We will make it default to true, so all cards will be dealt
        # face up
        self.player_type = True

