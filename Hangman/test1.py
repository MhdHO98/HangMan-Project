#!/usr/bin/env python3

from Classes import HMPlayer, HMHumanPlayer, HMAIPlayer
from game import HMGame

players = [HMAIPlayer("AI"), HMHumanPlayer("Moha")]
game = HMGame(players)
game.play()
