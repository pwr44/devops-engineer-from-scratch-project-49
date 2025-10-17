from random import randint

GAME_TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MIN_NUMBER = 2
MAX_NUMBER = 50


def get_random_number():
    return randint(MIN_NUMBER, MAX_NUMBER)


def is_prime(num):
    counter = 2
    while counter <= num / 2:
        if num % counter == 0:
            return False
        counter += 1
    return True


def get_game_data():
    game_question = get_random_number()
    game_answer = 'yes' if is_prime(game_question) else 'no'
    return [str(game_question), game_answer]
