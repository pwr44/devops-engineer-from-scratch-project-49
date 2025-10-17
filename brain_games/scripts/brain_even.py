from brain_games.engine import engine
from brain_games.games.brain_even import GAME_TASK, get_game_data


def main():
    engine(GAME_TASK, get_game_data)


if __name__ == "__main__":
    main()
