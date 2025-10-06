from random import randint

from brain_games.engine import engine

GAME_TASK = 'Find the greatest common divisor of given numbers.'
MIN_NUMBER = 2
MAX_NUMBER = 10


def get_random_number():
    return randint(MIN_NUMBER, MAX_NUMBER)


def get_second_number(first_number, random_member):
    second_number = get_random_number() * random_member
    while second_number == first_number:
        second_number = get_random_number() * random_member
    return second_number


def get_gcd(num_1, num_2):
    max_num = num_1 if num_1 > num_2 else num_2
    gcd = 1
    counter = 2
    while counter <= max_num / 2:
        if num_1 % counter == 0 and num_2 % counter == 0:
            gcd = counter
        counter += 1
    return gcd


def get_game_data():
    random_member = get_random_number()
    first_number = get_random_number() * random_member
    second_number = get_second_number(first_number, random_member)
    gcd = get_gcd(first_number, second_number)
    game_question = f'{first_number} {second_number}'
    game_answer = str(gcd)
    return [game_question, game_answer]


def main():
    engine(GAME_TASK, get_game_data)


if __name__ == "__main__":
    main()
