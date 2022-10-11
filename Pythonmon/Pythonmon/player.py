from random import random

from pokemon import Pokemon

class Player:

    def __init__(self, name, active_pokemon, other_pokemon):
        self.name = name
        self.active_pokemon = active_pokemon
        self.other_pokemon = other_pokemon
        self.move = "a"
        self.move_speed = 0

    def can_continue(self):
        """Player can't continue if no Pokémon are healthy."""
        return self.active_pokemon.is_alive() or self.other_pokemon

    def choose_move(self):
        """"Player commits to a move that is later executed."""
        print(f"{self.name}'s team:")
        self.list_team()
        while True:
            print("Type 'a' to attack, or an inactive Pokémon's id to "
                  "switch.")
            self.move = input()
            if self.move == "a":
                # Player chose to attack, this is a valid move.
                break
            try:
                switch_id = int(self.move)
                if switch_id in range(0, len(self.other_pokemon)):
                    # Player chose to switch, this is a valid move.
                    break
            except ValueError:
                pass
            print("Invalid input")
        # Set speed of player move.
        self.move_speed = (
            self.active_pokemon.speed
            + (0 if self.move == "a" else 1000) # Switching priority
            + random() # Tie breaker
         )

    def switch_after_faint(self):
        """Force player to switch."""
        print(f"{self.name}'s team:")
        self.list_team()
        switch_id = 0
        while True:
            print("Choose an inactive Pokémon's id to switch.")
            try:
                switch_id = int(input())
                if switch_id in range(0, len(self.other_pokemon)):
                    break
            except ValueError:
                pass
            print("Invalid input")
        # Set move to switch action, player can't attack anymore this round.
        self.move = str(switch_id)
        self.active_pokemon = self.other_pokemon[switch_id]
        del self.other_pokemon[switch_id]


    def switch(self):
        """Relplace active Pokémon with another Pokémon."""
        temp = self.active_pokemon
        self.active_pokemon = self.other_pokemon[int(self.move)]
        self.other_pokemon[int(self.move)] = temp
        print(f"{self.name} swithed {temp.name} out for "
              f"{self.active_pokemon.name}!")

    def get_attack(self):
        """Get the attack damage."""
        damage = self.active_pokemon.attack()
        return damage

    def take_damage(self, damage):
        """Player's active Pokémon recieves damage."""
        health_lost = self.active_pokemon.take_damage(damage)
        print(f"{self.name}'s {self.active_pokemon.name} lost {health_lost}% "
              "HP!")
        if self.active_pokemon.is_alive():
            print(f"{self.name}'s {self.active_pokemon.name} has "
                  f"{self.active_pokemon.remaining_hp_ratio()}% HP left!")
        else:
            print(f"{self.name}'s {self.active_pokemon.name} fainted!")
            if self.can_continue():
                self.switch_after_faint()

    def list_team(self):
        print("[id|Pokémon | HP/max|dmg|acc|spd|Type  ]")
        print(f"[ a|{self.active_pokemon.description()}]")
        for i, pokemon in enumerate(self.other_pokemon):
            print(f"[ {i}|{pokemon.description()}]")
