#!/usr/bin/env python3

from Hangman.Classes import HMPlayer, HMHumanPlayer, HMAIPlayer, HMGame

players = [HMAIPlayer("AI"), HMHumanPlayer("Moha")]
game = HMGame(players)
game.play()
