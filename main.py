from models.hero import Hero

players_name = input("What's the player's name? ")

print("What's the player's class:\n[1] Warrior\n[2] Wizard\n[3] Archer\n[4] Dark Elf\n[5] High Elf")
player_class_choice = input("Type your choice here: ----> ")

class_table = {
    "1": {"Classe": "Warrior", "HP": 100, "attack": 7},
    "2": {"Classe": "Wizard", "HP": 70, "attack": 10 },
    "3": {"Classe": "Archer", "HP": 65, "attack": 12 },
    "4": {"Classe": "Dark Elf", "HP": 85, "attack": 8 },
    "5": {"Classe": "High Elf", "HP": 80, "attack": 9 },
}

chosen_status = class_table.get(player_class_choice)

if chosen_status == None:
    print("Invalid choice! You are now a Peasant")
    chosen_class = "Peasant"
    base_HP = 30
    base_attack = 2

else:
    chosen_class = chosen_status["Classe"]
    base_HP = chosen_status["HP"]
    base_attack = chosen_status["attack"]

player = Hero(players_name, base_HP, chosen_class, base_attack)

while True:
     
    print("\n--- !!! WELCOME TO RPG BATTLE SYSTEM !!! ---")
    print("'1' Attack" '\n' "'2' Quit")

    player_choice = input("Type your choice here: ----> ")

    if player_choice == "1":
        player.attack_enemy()

    elif player_choice == "2" or player_choice == "quit":
        print("Shutting down...")
        break

    else:
        print("Invalid command. Try again!")
        print("-" * 20)
