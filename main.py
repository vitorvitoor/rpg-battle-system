from models.hero import Hero

players_name = input("What's the player's name? ")

print("What's the player's class:\n[1] Warrior\n[2] Wizard\n[3] Archer\n[4] Dark Elf\n[5] High Elf")
player_class_choice = input("Type your choice here: ----> ")

if player_class_choice == "1":
    chosen_class = "Warrior"
    base_hp = 100
    base_attack = 7

elif player_class_choice == "2":
    chosen_class = "Wizard"
    base_hp = 70  
    base_attack = 10

elif player_class_choice == "3":
    chosen_class = "Archer"
    base_hp = 65
    base_attack = 12

elif player_class_choice == "4":
    chosen_class = "Dark Elf"
    base_hp = 85  
    base_attack = 9

elif player_class_choice == "5":
    chosen_class = "High Elf"
    base_hp = 80
    base_attack = 10

else:
    print("Invalid choice! You are now a Peasant.")
    chosen_class = "Peasant"
    base_hp = 30
    base_attack = 2

player = Hero(player_class_choice, base_hp, chosen_class, base_attack)

while True:
     
    print("\n--- !!! WELCOME TO RPG BATTLE SYSTEM !!! ---")
    print("'1' Attack" '\n' "'2' Quit")

    player_choice = input("Type you choice here: ----> ")

    if player_choice == "1":
        player.attack_enemy()

    elif player_choice == "2" or player_choice == "quit":
        print("Shutting down...")
        break

    else:
        print("Invalid command. Try again!")
        print("-" * 20)
