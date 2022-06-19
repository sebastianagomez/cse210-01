import random

class Hilo:
    """"A card with a value between 1 and 13.

    The responsibility of the Card is to keep track of the value of the current and the next card.
   
    Attributes:
        value (int): The number of spots on the side facing up.
    """

    def __init__(self):
        """Constructs a new instance of Card.

        Args:
            self (Card): An instance of Card.
        """
        self.value = 0

    def roll(self):
        """Generates a new random value of the card.
        
        Args:
            self (Card): An instance of Card.
        """
        self.value = random.randint(1, 13)