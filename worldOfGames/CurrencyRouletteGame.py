import requests


class CurrencyRouletteGame:

    def __init__(self, difficulty=5):
        self.difficulty = difficulty

    def get_money_interval(self, current_currency_rate):
        return [
            (current_currency_rate - (5 - int(self.difficulty)), current_currency_rate + (5 - int(self.difficulty)))]

    def get_guess_from_user(self):
        print("guess the amount of the USD")
        guessed_amount = input()
        return float(guessed_amount)

    def play(self):
        print("Choose a difficulty level from 1 to 5")
        diff = input()
        self.difficulty = diff
        url = 'https://api.exchangerate.host/convert?from=USD&to=ILS'
        current_currency_rate = (requests.get(url)).json()['result']
        currency_surrounding_range = self.get_money_interval(current_currency_rate)
        user_guess = self.get_guess_from_user()
        try:
            assert currency_surrounding_range[0][0] <= user_guess < currency_surrounding_range[0][1]
            print("You did it!")
        except AssertionError:
            print("Ohh... Maybe next time")


# if __name__ == '__main__':
#     first_guess = CurrencyRouletteGame()
#     first_guess.play()
