from Live import test_load_game, welcome
from GuessGame import *
from worldOfGames.MemoryGame import MemoryGame

print(welcome("Guy"))
test_load_game()
guess = GuessGame(10)
print(guess.play())

memory_game = MemoryGame()
print(memory_game.play())
