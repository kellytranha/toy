from player import Player
from deck import Deck
from random import shuffle

class Game:
    def __init__(self):
        self.player1 = Player("Steven")
        self.player2 = Player("Kelly")
        self.deck = Deck()
        shuffle(self.deck.cards)


    def start(self):
        print("Game is starting")
        self.player1.hello()
        self.player2.hello()
        print(self.deck)
        for _ in range(3):
            self.player1.get_a_card(self.deck.draw_a_card())
            self.player2.get_a_card(self.deck.draw_a_card())
        

        player1_total = self.player1.get_hand_total()
        player2_total = self.player2.get_hand_total()
        print(self.player1.name, ": ", self.player1.hand, "-", player1_total)
        print(self.player2.name, ": ", self.player2.hand, "-", player2_total)
    
        if player1_total > player2_total:
            print(self.player1.name, "won")
        elif player2_total > player1_total:
            print(self.player2.name, "won")
        else:
            print("draw")

