from time import sleep

class Battle:

    def __init__(self, player_a, player_b):
        self.players = [player_a, player_b]

    def start(self):
        while True:
            self.play_round();
            for player in self.players:
                if not player.can_continue():
                    print(f"{player.name} has no Pokémon left and lost the "
                          "battle.")
                    return

    def play_round(self):
        print("Round start!")
        for player in self.players:
            print(f"{player.name}'s {player.active_pokemon.name} has "
                  f"{player.active_pokemon.remaining_hp_ratio()}% HP "
                  f"remaining (and {len(player.other_pokemon)} additional "
                  "Pokémon left).")
        self.choose_moves()
        self.execute_moves()

    def choose_moves(self):
        for player in self.players:
            player.choose_move()

    def execute_moves(self):
        ordered_player_ids = sorted(
            [0, 1],
            key = lambda i: -self.players[i].move_speed)

        for player_id in ordered_player_ids:
            player = self.players[player_id]
            if player.move != "a":
                player.switch()
                sleep(0.5)

        for player_id in ordered_player_ids:
            player = self.players[player_id]
            if player.move == "a":
                damage = player.get_attack()
                sleep(0.5)
                if damage > 0:
                    other = self.players[1 - player_id]
                    other.take_damage(damage)
                    sleep(0.5)
                    if not other.can_continue():
                        sleep(0.5)
                        break
