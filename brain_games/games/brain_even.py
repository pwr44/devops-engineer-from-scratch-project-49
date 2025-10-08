from random import randint

from brain_games.engine import engine

GAME_TASK: str = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_NUMBER = 1
MAX_NUMBER = 10


def get_num():
    return randint(MIN_NUMBER, MAX_NUMBER)


def is_even(num):
    return num % 2 == 0


def get_game_data():
    num = get_num()
    answer = 'yes' if is_even(num) else 'no'
    return [str(num), answer]


def main():
    engine(GAME_TASK, get_game_data)


if __name__ == "__main__":
    main()
