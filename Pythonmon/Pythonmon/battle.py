class Battle:

    def __init__(self, player_a, player_b):
        self.players = [player_a, player_b]

    def start(self):
        while True:
            self.play_round();

    def play_round(self):
        print("Round start!")
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

        for player_id in ordered_player_ids:
            player = self.players[player_id]
            if player.move == "a":
                damage = player.get_attack()
                if damage > 0:
                    self.players[1 - player_id].take_damage(damage)
