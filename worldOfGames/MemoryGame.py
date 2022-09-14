import os
import random
import time


class MemoryGame:
    difficulty = None
    random_sequence = []
    user_sequence = []

    def __init__(self, difficulty=5):
        self.difficulty = difficulty
        self.random_sequence = []
        self.user_sequence = []

    def generate_sequence(self):
        random_sequence = []
        for i in range(self.difficulty):
            random_value = random.randint(1, 101)
            random_sequence.append(random_value)
        self.random_sequence = random_sequence

    def get_list_from_user(self):
        user_sequence = []
        for item in range(self.difficulty):
            user_input = input()
            user_sequence.append(int(user_input))
        self.user_sequence = user_sequence

    def is_list_equal(self):
        return self.random_sequence == self.user_sequence

    def play(self):
        self.generate_sequence()
        print(f"Try to remember all the numbers from the list below \n {self.random_sequence}")
        time.sleep(5)
        os.system('clear')
        print("Enter the numbers from the previous list")
        self.get_list_from_user()
        return self.random_sequence == self.user_sequence

#
# if __name__ == '__main__':
#     m = MemoryGame(3)
#     if m.play():
#         print("You did it!")
#     else:
#         print("Ohh... Maybe next time")
