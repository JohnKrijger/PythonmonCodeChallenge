from pokemon import Pokemon
from player import Player
from battle import Battle

def main():
    player_a = Player(
        "Trainer A",
        Pokemon("Lando-T", 642, 230, 100, 241),
        [
            Pokemon("Toxapex", 810, 116, 100, 106),
        ]
    )
    player_b = Player(
        "Trainer B",
        Pokemon("Lando-T", 642, 230, 100, 241),
        [
            Pokemon("Toxapex", 810, 116, 100, 106),
        ]
    )
    battle = Battle(player_a, player_b)
    battle.start()

if __name__ == "__main__":
    main()