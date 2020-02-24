from card import Card

values = "2 3 4 5 6 7 8 9 10 J Q K A".split()
suits = "Heart Diamond Club Spade".split()


class Deck:
    def __init__(self):
        self.cards = []
        for value in values:
            for suit in suits:
                card = Card(suit, value)
                self.cards.append(card)

    def __repr__(self):
        return str(self.cards)