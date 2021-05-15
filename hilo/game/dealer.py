import random

class Dealer:
    """A code template for a person who deals a card. The responsibility of this 
    class of objects is to pick the cards to show the player.
    """
    def __init__(self):
        """The class constructor.
        
        Args:
            self (Director): An instance of Director.
        """
        self.cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    def get_nextCard(self):
        """Determines the random number to give the player.

        Args:
            self (Thrower): An instance of Thrower.
        Returns:
            number: Returns a random number from the list.
        """
        random.shuffle(self.cards)
        return self.cards[0]