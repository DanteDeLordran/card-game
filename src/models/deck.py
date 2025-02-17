import random

from pygame import Surface

from card import Card


class Deck:

    SUITS = ('Diamonds', 'Hearts', 'Spades', 'Clubs')

    STANDARD = {
        'Ace' : 1,
        '2' : 2,
        '3' : 3,
        '4' : 4,
        '5' : 5,
        '6' : 6,
        '7' : 7,
        '8' : 8,
        '9' : 9,
        '10' : 10,
        'Jack' : 11,
        'Queen' : 12,
        'King' : 13,
    }

    def __init__(self, window : Surface, rank_value = STANDARD):
        self.starting_deck = []
        self.playing_deck = []

        for suit in Deck.SUITS:
            for rank, value in rank_value.items():
                card = Card(window, rank, suit, value)
                self.starting_deck.append(card)

        self.shuffle()

    def shuffle(self) -> None:
        self.playing_deck = self.starting_deck.copy()
        for card in self.playing_deck:
            card.conceal()
        random.shuffle(self.playing_deck)

    def get_card(self) -> Card:
        if len(self.playing_deck) == 0:
            raise IndexError("No more cards")
        card = self.playing_deck.pop()
        return card

    def return_card_to_desk(self, card : Card) -> None:
        self.playing_deck.insert(0, card)