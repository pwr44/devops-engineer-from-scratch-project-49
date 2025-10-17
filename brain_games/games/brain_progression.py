from random import randint

GAME_TASK = 'What number is missing in the progression?'
MIN_NUMBER = 1
MAX_NUMBER = 10
PROGRESSION_MEMBERS_COUNT = 10


def get_random_number():
    return randint(MIN_NUMBER, MAX_NUMBER)


def get_progression():
    first_member = get_random_number()
    step = get_random_number()
    progression = []
    for i in range(PROGRESSION_MEMBERS_COUNT):
        progression.append(str(first_member + step * i))
    return progression


def get_game_data():
    progression = get_progression()
    missed_member_position = get_random_number() - 1
    missed_member = progression[missed_member_position]
    progression[missed_member_position] = '..'
    return [' '.join(progression), missed_member]
