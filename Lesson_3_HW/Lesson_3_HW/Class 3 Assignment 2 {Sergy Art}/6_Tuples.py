"""
# Exercise: Create a simple role-playing game where the player
encounters a series of enemies. Each enemy is represented as a
tuple with (name, health). The player attacks each enemy,
reducing their health to zero to defeat them.
"""
from time import sleep

def rpg_game():
    print("""Welcome to the RPG game
here you will fight multiple monsters on your adventure""")

    name = str(input("Please provide me with your hero's name: \n"))
    player = (name, 100)
    player_weapon = ("sword", 15)

    enemy_1 = ("Goblin", 20, "Wooden Stick", 1)

    enemy_2 = ("Troll", 30, "Stone Hammer", 5)

    enemy_3 = ("Dragon", 100, "Fire Breathe", 10)

    enemies = [enemy_1, enemy_2, enemy_3]

    for enemy in enemies:
        name, enemy_health, enemy_weapon, enemy_weapon_damage = enemy

        print(f"\nOn your adventure you encounter a {name}")
        sleep(2)
        print("combat begins:")
        sleep(1)

        while enemy_health > 0 and player[1] > 0:

            #player attack
            enemy_health -= player_weapon[1]
            print(f"You hit the {name} with your {player_weapon[0]}!")
            sleep(2)
            print(f"{name} loses {player_weapon[1]} health, remaining health: {enemy_health}")
            sleep(1)

            if enemy_health <= 0:
                print(f"You defeated the {name}")
                sleep(3)
                break

            #enemy attack
            player = (player[0], player[1] - enemy_weapon_damage)
            print(f"The {name} hits you with their {enemy_weapon}!")
            sleep(2)
            print(f"You lose {enemy_weapon_damage} health, remaining health: {player[1]}")
            sleep(1)
            print()

            if player[1] <= 0:
                print("You have been defeated!")
                return

        enemy = (name, enemy_health, enemy_weapon, enemy_weapon_damage)
    print("\nCongratulations, you have defeated all the enemies!")

rpg_game()
