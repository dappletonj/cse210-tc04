import random

class Dealer:
    def __init__(self):
        self.cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    # Display current card
    def get_nextCard(self):
        random.shuffle(self.cards)
        return self.cards[0]

        