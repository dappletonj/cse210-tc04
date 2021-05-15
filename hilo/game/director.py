from game.dealer import Dealer

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to keep track of the score, control the 
    sequence of play, and determine if the player can keep playing.
    
    Attributes:
        score (number): The total number of points earned.
        keep_playing (Boolean): Whether or not the player wants to keep playing.
        dealer (Dealer): An instance of the class of objects known as Dealer.
    """
    def __init__(self):
        """The class constructor.
        
        Args:
            self (Director): An instance of Director.
        """
        self.keep_playing = True
        self.score = 300
        self.dealer = Dealer()

    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): An instance of Director.
        """
        while self.keep_playing:
            current_card = self.dealer.get_nextCard()
            print(f"The card is: {current_card}")
            hl_inputs = self.get_inputs()
            next_card = self.dealer.get_nextCard()
            print(f"Next card was: {next_card}")
            higher = self.isHigher(current_card, next_card)
            isCorrect = self.is_correct(hl_inputs, higher)
            self.do_updates(isCorrect)
            self.do_outputs()
            self.keepPlaying()
            print()
            
    def keepPlaying(self):
        """Determines whether the player can keep playing, if they have more
        points than 0, and if so gives the player gets the choice to keep playing 
        or end the game.
        
        Args:
            self (Director): An instance of Director.
        """
        if self.score <= 0:
            self.keep_playing = False
        else:
            userInput = input("Keep playing? [y/n] ")
            if userInput == 'y':
                self.keep_playing = True
            else:
                self.keep_playing = False

    def is_correct(self, hl_inputs, higher):
        """This function determines whether the player guessed correctly or 
        incorrectly about the next card being high or low. 
        
        Args:
            self (Director): An instance of Director.
            hl_inputs: An input from the user that will either 
            be an h or l.
            higher: Determined which card is higher or lower.
        Returns: 
            boolean: True if the player guesses right, and false
            if the player guesses wrong.
        """
        if hl_inputs == 'h' and higher:
            return True
        elif hl_inputs == 'h' and not higher:
            return False
        elif hl_inputs == 'l' and higher:
            return False
        elif hl_inputs == 'l' and not higher:
            return True
        
    def get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means whether the player thinks the next card is higher or lower.

        Args:
            self (Director): An instance of Director.
        Returns:
            string: Returns an h or l depending on what the user inputs.
        """
        userInput = input("Higher or lower? [h/l] ")
        return userInput

    def isHigher(self, current_card, next_card):
        """Determines whether the current card and next card are higher or lower
        than each other.
        
        Args:
            self (Director): An instance of Director.
            current_card: Gives the current card, the one the user
            can see.
            next_card: Gives the next card.
        Returns:
            boolean: True if the current card is less than the next 
            card, and False if the current card is greater than or 
            equal to the next card.
        """
        if current_card < next_card:
            status = True
        elif current_card >= next_card:
            status = False
        return status

    def do_updates(self, isCorrect):
        """Updates the important game information for each round of play. In 
        this case, that means calculating and updating the score.

        Args:
            self (Director): An instance of Director.
            isCorrect: Determined whether the player guessed right
            or wrong.
        """
        if isCorrect == True:
            self.score += 100
        elif isCorrect == False:
            self.score -= 75

    def do_outputs(self):
        """Outputs what the score is for the player to see.

        Args:
            self (Director): An instance of Director.
        """
        print(f"Your score is: {self.score}")