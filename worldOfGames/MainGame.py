from Live import load_game, welcome
from GuessGame import *
from worldOfGames.MemoryGame import MemoryGame

print(welcome("Guy"))
load_game()
guess = GuessGame(10)
print(guess.play())

memory_game = MemoryGame()
print(memory_game.play())
