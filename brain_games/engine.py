import prompt

GAMES_COUNT: int = 3


def get_user_answer():
    return prompt.string('Your answer: ')


def engine(GAME_TASK, get_game_data):
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print(GAME_TASK)
    is_user_win = True
    for _ in range(GAMES_COUNT):
        game_question, game_answer = get_game_data()
        print(f'Question: {game_question}')
        user_answer = get_user_answer()
        if user_answer == game_answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer is '{game_answer}'.")
            is_user_win = False
            break
    final_message = 'Congratulations' if is_user_win else "Let's try again"
    print(f'{final_message}, {user_name}!')
