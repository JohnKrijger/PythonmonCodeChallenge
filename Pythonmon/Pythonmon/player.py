from random import random

from pokemon import Pokemon

class Player:

    def __init__(self, name, active_pokemon, other_pokemon):
        self.name = name
        self.active_pokemon = active_pokemon
        self.other_pokemon = other_pokemon
        self.move = "a"
        self.move_speed = 0

    def choose_move(self):
        print(f"{self.name}'s team:")
        self.list_team()
        while True:
            print("Type 'a' to attack, or an inactive Pokémon's id to "
                  "switch.")
            self.move = input()
            if self.move == "a":
                break
            try:
                switch_id = int(self.move)
                if switch_id in range(0, len(self.other_pokemon)):
                    break
            except ValueError:
                pass
            print("Invalid input")
        self.move_speed = (
            self.active_pokemon.speed
            + (0 if self.move == "a" else 1000) # Switching priority
            + random() # Tie breaker
         )

    def switch(self):
        temp = self.active_pokemon
        self.active_pokemon = self.other_pokemon[int(self.move)]
        self.other_pokemon[int(self.move)] = temp
        print(f"{self.name} swithed {temp.name} out for "
              f"{self.active_pokemon.name}!")

    def get_attack(self):
        damage = self.active_pokemon.attack()
        if damage > 0:
            print(f"{self.name}'s {self.active_pokemon.name} dealt {damage} "
                  "damage!")
        else:
            print(f"{self.name}'s {self.active_pokemon.name} missed!")
        return damage

    def take_damage(self, damage):
        health_lost = self.active_pokemon.take_damage(damage)
        print(f"{self.name}'s {self.active_pokemon.name} lost {health_lost}% "
              "HP!")
        if self.active_pokemon.is_alive():
            print(f"{self.name}'s {self.active_pokemon.name} has "
                  f"{self.active_pokemon.remaining_hp_ratio()}% HP left!")
        else:
            print(f"{self.name}'s {self.active_pokemon.name} fainted!")

    def list_team(self):
        print("[id|pokémon | HP/max|dmg|acc|spd]")
        print(f"[ a|{self.active_pokemon.description()}]")
        for i, pokemon in enumerate(self.other_pokemon):
            print(f"[ {i}|{pokemon.description()}]")
