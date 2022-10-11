from pokemon import Pokemon
from player import Player

def main():
    players = [
        Player(
            "Trainer A",
            Pokemon("Lando-T", 642, 230, 100, 241),
            [
                Pokemon("Toxapex", 810, 116, 100, 106),
            ]
        ),
        Player(
            "Trainer B",
            Pokemon("Lando-T", 642, 230, 100, 241),
            [
                Pokemon("Toxapex", 810, 116, 100, 106),
            ]
        ),
        ]

    for player in players:
        player.list_team()

    while True:
        print("Round start!")
        for player in players:
            player.choose_move()

        ordered_player_ids = sorted(
            [0, 1],
            key = lambda i: -players[i].move_speed)

        for player_id in ordered_player_ids:
            player = players[player_id]
            if player.move != "a":
                player.switch()

        for player_id in ordered_player_ids:
            player = players[player_id]
            if player.move == "a":
                damage = player.get_attack()
                if damage > 0:
                    players[1 - player_id].take_damage(damage)


if __name__ == "__main__":
    main()