from random import randint

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


def get_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def get_game_data():
    random_member = get_random_number()
    first_number = get_random_number() * random_member
    second_number = get_second_number(first_number, random_member)
    gcd = get_gcd(first_number, second_number)
    game_question = f'{first_number} {second_number}'
    game_answer = str(gcd)
    return [game_question, game_answer]
