from game.dealer import Dealer

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to keep track of the score and control the 
    sequence of play.
    
    Attributes:
        score (number): The total number of points earned.
        keep_playing (Boolean): Whether or not the player wants to keep playing.
        dealer (Dealer): An instance of the class of objects known as Dealer.
    """
    def __init__(self):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self.keep_playing = True
        self.score = 300
        self.dealer = Dealer()

    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
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
            
    def keepPlaying(self):
        if self.score <= 0:
            self.keep_playing = False
        else:
            userInput = input("Keep playing? [y/n] ")
            if userInput == 'y':
                self.keep_playing = True
            else:
                self.keep_playing = False



    def is_correct(self, hl_inputs, higher):
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
        that means showing the card.

        Args:
            self (Director): An instance of Director.
        """
        userInput = input("Higher or lower? [h/l]")
        return userInput

    def isHigher(self, current_card, next_card):
        if current_card < next_card:
            status = True
        elif current_card >= next_card:
            status = False
        return status

    def do_updates(self, isCorrect):
        """Updates the important game information for each round of play. In 
        this case, that means updating the score.

        Args:
            self (Director): An instance of Director.
        """
        # Calculate the score
        if isCorrect == True:
            self.score += 100
        elif isCorrect == False:
            self.score -= 75

    def do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means the dice that were rolled and the score.

        Args:
            self (Director): An instance of Director.
        """
        print(f"Your score is: {self.score}")