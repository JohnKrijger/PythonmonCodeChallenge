from random import randint

class Pokemon:
    
    def __init__(self, name, max_health, damage, hit_chance, speed):
        self.name = name # Name of the pokémon
        self.max_health = max_health # Amount of damage the pokémon can take
        self.health = max_health # Current health
        self.damage = damage # Damage of an attack
        self.hit_chance = hit_chance # Percentage chance to hit
        self.speed = speed # Determines attack order
    

    def attack(self):
        """Returns the damage from an attack or 0 if it misses."""
        return self.damage if randint(1, 100) <= self.hit_chance else 0

    def take_damage(self, damage):
        """
        Reduce health by given damage amount, returns percentage of max health
        lost.
        """
        old_health = self.health
        self.health -= damage
        if self.health < 0:
            self.health = 0
        return round((old_health - self.health) * 100 / self.max_health)

    def remaining_health_ratio(self):
        """Returns the ratio of health remaining"""
        return self.health / self.max_health

    def is_alive(self):
        return self.health > 0

    def remaining_hp_ratio(self):
        return round(self.health * 100 / self.max_health)

    def description(self):
        return (f"{self.name:8}|{self.health:3}/{self.max_health:3}|"
                f"{self.damage:3}|{self.hit_chance:3}|{self.speed}")



