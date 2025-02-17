import pygame
import pygwidgets
from pygame import Surface
from pathlib import Path


class Card:

    BACK_OF_CARD = pygame.image.load(Path(__file__).parent.parent / "assets" / "images" / "BackOfCard.png")

    def __init__(self, window : Surface, rank : str, suit : str, value):
        self.window = window
        self.rank = rank
        self.suit = suit
        self.value = value
        self.name = f"{self.rank} of {self.suit}"
        self.images = pygwidgets.ImageCollection(
            window,
            (0,0),
            {
                'font' : Path(__file__).parent.parent / "assets" / "images" / f"{self.name}",
                'back' : Card.BACK_OF_CARD
            },
            'back'
        )

    def conceal(self):
        self.images.replace('back')

    def reveal(self):
        self.images.replace('back')

    def get_name(self):
        return self.name

    def get_value(self):
        return self.value

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def set_loc(self, location : (int, int)):
        self.images.setLoc(location)

    def get_loc(self):
        return self.images.getLoc()

    def draw(self):
        self.images.draw()