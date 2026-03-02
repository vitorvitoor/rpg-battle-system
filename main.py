from models.hero import Hero

int(input("What's the first player's name? "))

player = Hero("Koukusen", 100, "Warrior", 8)

contador = 0 

while True:
     
    print("--- !!! WELCOME TO RPG BATTLE SYSTEM !!! ---")
    print("'1' Attack" '\n' "'2' Quit")

    player_choice = input("Type you choice here: ----> ")

    if player_choice == "1":
        player.attack_enemy()

    elif player_choice == "2" or player_choice == quit:
        print("Saindo do jogo...")

    else:
        print("Comando inválido. Tente novamente!")
        print("-" * 20)





