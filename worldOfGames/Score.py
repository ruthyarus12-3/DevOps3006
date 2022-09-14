from worldOfGames import Utils


def add_score(difficulty):
    try:
        with open(Utils.SCORES_FILE_NAME, 'r+') as file:
            file.read().splitlines()

    except FileNotFoundError:
        with open(Utils.SCORES_FILE_NAME, 'w') as file:
            calc = (int(difficulty) * 3) + 5
            file.write(str(calc))
