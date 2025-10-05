from random import randint

from brain_games.engine import engine

GAME_TASK: str = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_num():
    return randint(1, 10)


def is_even(num):
    return num % 2 == 0


def get_game_data():
    num = get_num()
    answer = 'yes' if is_even(num) else 'no'
    return [num, answer]


def main():
    engine(GAME_TASK, get_game_data)


if __name__ == "__main__":
    main()
