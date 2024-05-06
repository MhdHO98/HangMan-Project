from .test import play

if __name__ == "__main__":
    
  players = [HMAIPlayer("AI"), HMHumanPlayer("Moha")]
  game = HMGame(players)
  game.play()
