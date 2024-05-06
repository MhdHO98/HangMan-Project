#!/usr/bin/env python3

from Hangman.Classes import HMPlayer,HMHumanPlayer,HMAIPlayer
import random

class HMGame:
    def __init__(self, players:list) -> None:
        self.word = random.choice(["dog", "cat", "house", "pencil", "music", "banana", "hospital"])
        self.players = players
        self.guessed_letters = []

    def display_word(self):
        return "".join(c if c in self.guessed_letters else '_' for c in self.word)
    
    def play(self):
        print("Game started! Guess the word.")
        while any(p.lives > 0 for p in self.players) and self.word != self.display_word():
            for p in self.players:
                if p.lives > 0:
                    print("---------------------------")
                    self.turn(p)
                    if self.word == self.display_word():
                        print(f"Congratulations {p.name}, you won!")
                        return
        print("Game over! The word was '{}'.".format(self.word))
        print("The player that has won the game is {}".format(max(self.players)))
    
    def turn(self, p: HMPlayer) -> None:
        print("Player {}. Word: {}".format(p.name, self.display_word()))
        l = p.propose_letter()
        if l not in self.guessed_letters:
            self.guessed_letters.append(l)
            if l in self.word:
                print(f"Good guess, {p.name}!\n")
            else:
                print(f"Wrong guess, {p.name}!\n")
                p.lives -= 1
        else:
            print(f"{p.name}, you've already guessed that letter.")
