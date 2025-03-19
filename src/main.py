import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.game import Game

if __name__ == "__main__":
    game = Game()
    game.run()