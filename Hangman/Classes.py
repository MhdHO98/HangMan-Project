import random
from time import sleep

class HMPlayer:
    """This is a generic player for the hangman game."""
    def __init__(self, name:str) -> None:
        """Constructor, needs the player's name."""
        self.name = name
        self.lives = 5

    def propose_letter(self):
        print("WARNING! To be reimplemented in a derived class")

    def __str__(self) -> str:
        return "{} has {} lives left.".format(self.name, self.lives)
    
    def __lt__(self, others):
        return self.lives < others.lives

class HMHumanPlayer(HMPlayer):
    """A class to represent a Hangman Human player."""
    def propose_letter(self) -> str:
        sleep(1)
        letter = ""
        while len(letter) != 1:
            letter = input("Propose a letter: ")
        return letter
    
class HMAIPlayer(HMPlayer):
    """A class to represent a Hangman AI player."""
    def __init__(self, name: str) -> None:
        super().__init__(name + "_bot")
        self.proposed_letters = []
    
    def propose_letter(self) -> str:
        letter = random.choice("abcdefghijklmnopqrstuvwxyz")
        while letter in self.proposed_letters:
            letter = random.choice("abcdefghijklmnopqrstuvwxyz")
        self.proposed_letters.append(letter)
        return letter

