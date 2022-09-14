from worldOfGames import Score
from worldOfGames.CurrencyRouletteGame import CurrencyRouletteGame
from worldOfGames.GuessGame import GuessGame
from worldOfGames.MemoryGame import MemoryGame


def welcome(name):
    return f"Hello {name} and welcome to the World of Games (WoG).\nHere you can find many cool games to play."


game_dict = {1: "memory_game",
             2: "guess_game",
             3: "currency_roulette_game"}

difficulty_dict = {1: "Easy",
                   2: "Moderate",
                   3: "Challenging",
                   4: "Demanding",
                   5: "Extreme"}


def memory_game(difficulty):
    memory_game = MemoryGame(difficulty)
    memory_game.play()


def guess_game(difficulty):
    guess_game = GuessGame(difficulty)
    guess_game.play()


def currency_roulette_game(difficulty):
    currency_roulette_game = CurrencyRouletteGame(difficulty)
    currency_roulette_game.play()


switcher = {
    "memory_game": memory_game(4),
    "guess_game": guess_game(4),
    "currency_roulette_game": currency_roulette_game(1)
}


def load_game():
    game = select_game()
    difficulty = select_difficulty()
    game_dict.get(int(game))
    print(
        f"You've selected {game_dict.get(int(game))} game with {difficulty_dict.get(int(difficulty))} difficulty stage")
    game = game_dict.get(int(game))
    if switcher.get(game, default)() is True:
        Score.add_score(difficulty)

def default():
    print("DEFAULT")
    memory_game = MemoryGame(1)
    memory_game.play()


def game_instructions():
    with open("/Users/ruthyarus/PycharmProjects/DevOps3006/worldOfGames/gameToPlay.txt") as my_file:
        for line in my_file.readlines():
            print(line.strip())


def select_game():
    game_instructions()
    try:
        selected_game = input()
        if int(selected_game) < 1 or int(selected_game) > 3:
            raise ValueError("Out of range. Please try again")
        return selected_game
    except ValueError:
        print("Out of range. Please try again")
        return select_game()


def select_difficulty():
    print("Please choose game difficulty from 1 to 5:")
    try:
        difficulty_game = input()
        if int(difficulty_game) < 1 or int(difficulty_game) > 5:
            raise ValueError("Out of range. Please try again")
        return difficulty_game
    except ValueError:
        print("Out of range. Please try again")
        return select_difficulty()


