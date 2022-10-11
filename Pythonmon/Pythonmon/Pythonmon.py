from copy import deepcopy

from pokemon import Pokemon
from player import Player
from battle import Battle

def main():
    all_pokemon = [
        Pokemon("Lando-T", 642, 230, 100, 241),
        Pokemon("Toxapex", 810, 116, 100, 106),
        Pokemon("Heatran", 480, 298, 75, 278),
        Pokemon("Kartana", 464, 253, 100, 348),
        Pokemon("D-pult", 356, 255, 100, 421),
        Pokemon("Rilla", 443, 321, 100, 269),
    ]

    player_a = Player(
        "Trainer A",
        deepcopy(all_pokemon[0]),
        [deepcopy(pokemon) for pokemon in all_pokemon[1:]]
    )
    player_b = Player(
        "Trainer B",
        deepcopy(all_pokemon[0]),
        [deepcopy(pokemon) for pokemon in all_pokemon[1:]]
    )
    battle = Battle(player_a, player_b)
    battle.start()

if __name__ == "__main__":
    main()