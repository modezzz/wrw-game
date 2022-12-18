from models import Player, Enemy
from exceptions import EnemyDown, GameOver


def get_player_name() -> str:
    player_name = input("Enter a name to start the game: ").strip()
    if len(player_name) < 1:
        print("A player's name must be at least one character.")
        return get_player_name()
    return player_name


def play() -> None:
    player_name = get_player_name()
    player = Player(player_name)
    enemy = Enemy()

    while True:
        try:
            player.attack(enemy)
            player.defence(enemy)
        except EnemyDown as defeat:
            print(defeat)
            enemy = Enemy()
        except GameOver as gg:
            print(gg)
            print(f"'{player_name.capitalize()}' your final score is {player.score}")
            break


if __name__ == "__main__":
    try:
        play()
    except KeyboardInterrupt("Empty value. Try again.") as err:
        print(err)
