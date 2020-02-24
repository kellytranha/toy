from player import Player
from deck import Deck


class Game:
    def __init__(self):
        self.player1 = Player("Steven")
        self.player2 = Player("Kelly")
        self.deck = Deck()

    def start(self):
        print("Game is starting")
        self.player1.hello()
        self.player2.hello()
        print(self.deck)
