from pokemon import Pokemon

def main():
    print("           [pokémon | HP/max|dmg|acc|spd]")
    attacking_mon = Pokemon("Lando-T", 642, 230, 100, 241)
    print(f"Attacking: [{attacking_mon.description()}]")
    defending_mon = Pokemon("Toxapex", 810, 116, 100, 106)
    print(f"Defending: [{defending_mon.description()}]")
    damage = attacking_mon.attack()
    if damage > 0:
        print(f"{attacking_mon.name} dealt {damage} damage!")
        health_lost = defending_mon.take_damage(damage)
        print(f"{defending_mon.name} lost {health_lost}% HP!")
        if not defending_mon.is_alive():
            print(f"{defending_mon.name} fainted!")
    else:
        print(f"{attacking_mon.name} missed!")
    print("           [pokémon | HP/max|dmg|acc|spd]")
    print(f"Attacking: [{attacking_mon.description()}]")
    print(f"Defending: [{defending_mon.description()}]")

if __name__ == "__main__":
    main()