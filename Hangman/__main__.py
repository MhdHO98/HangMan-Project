#!/usr/bin/env python3

from Classes import HMPlayer, HMHumanPlayer, HMAIPlayer
from game import HMGame

def main():
  
    players = [HMAIPlayer("AI"), HMHumanPlayer("Moha")]
    game = HMGame(players)
    game.play()

if __name__ == '__main__':
    main()
