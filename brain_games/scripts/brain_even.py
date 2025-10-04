from random import randint

import prompt

from brain_games.cli import welcome_user
from brain_games.module import greet

GAMES_COUNT: int = 3


def get_num():
    return randint(1, 10)


def is_even(num):
    return num % 2 == 0


def main():
    greet()
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for _ in range(ROUNDS):
        num = get_num()
        print(f'Question: {num}')
        answer = prompt.string('Your answer: ')
        if answer == is_even(num):
            print('Correct!')
        else:
            print('Wrong!')
    print(f'Congratulations, {name}!')


if __name__ == "__main__":
    main()
