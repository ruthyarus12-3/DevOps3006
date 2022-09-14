import random


class GuessGame:
    difficulty = None
    secret_number = None
    user_guess = None

    def __init__(self, difficulty=5, secret_number=None, user_guess=None):
        self.difficulty = difficulty
        self.secret_number = secret_number
        self.user_guess = user_guess

    def generate_number(self):
        self.secret_number = str(random.randint(1, self.difficulty))

    def get_guess_from_user(self):
        print(f"Enter a number between 1 to {self.difficulty}")
        user_guess = int(input())
        while int(user_guess) < 1 or int(user_guess) > self.difficulty:
            print("Out of range. Please try again")
            user_guess = input()
        self.user_guess = user_guess

    def compare_results(self):
        return self.secret_number == self.user_guess

    def play(self):
        self.generate_number()
        self.get_guess_from_user()
        return int(self.secret_number) == int(self.user_guess)

# if __name__ == '__main__':
#     first_guess = GuessGame()
#     print(first_guess.play())
