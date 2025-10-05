from random import randint

from brain_games.engine import engine

GAME_TASK = 'What is the result of the expression?'
OPERATORS = [' + ', ' - ', ' * ']
MIN_NUMBER = 1
MAX_NUMBER = 20


def get_game_data():
    first_member = randint(MIN_NUMBER, MAX_NUMBER)
    second_member = randint(MIN_NUMBER, MAX_NUMBER)
    curr_operator = OPERATORS[randint(0, 2)]
    game_question = str(f'{first_member}{curr_operator}{second_member}')
    game_answer = ''
    match curr_operator:
        case ' + ':
            game_answer = str(first_member + second_member)
        case ' - ':
            game_answer = str(first_member - second_member)
        case ' * ':
            game_answer = str(first_member * second_member)
    return [game_question, game_answer]


def main():
    engine(GAME_TASK, get_game_data)


if __name__ == "__main__":
    main()
