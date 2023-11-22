import random

def choose_pokemon():
    name = input("What is your name: ")
    print("1. Pikachu")
    print("2. Bulbasaur")
    print("3. Charmander")
    choice = int(input("Pick your pokemon 1-3: "))
    if choice == 1:
        print("You chose Pikachu")
        return name, "Pikachu"
    elif choice == 2:
        print("You chose Bulbasaur")
        return name, "Bulbasaur"
    elif choice == 3:
        print("You chose Charmander")
        return name, "Charmander"
    else:
        print("Invalid Choice")
        return name, "Invalid Choice"

def game_intro(player_name, pokemon_type):
    print(f"Welcome to the Pokemon world {player_name}! {pokemon_type} will be your first pokemon.")
    print("Pokemon trainers have been around since the dawn of time. Level up and build your team to make it to the top.")
    print()

def pokemon_battle(pokemon_type):
    print("You have encountered a wild Wombat!")
    print()

    if pokemon_type == "Pikachu":
        attack_number = int(input("Choose Thunderbolt (1) or Quick Attack (2): "))
        if attack_number == 1:
            print("It was a critical hit! Wombat has fainted!")
            damage_taken = 0
            return damage_taken
        elif attack_number == 2:
            print("You missed. Pikachu has taken damage.")
            damage_taken = random.randint(20, 50)
            return damage_taken
        else:
            print("Invalid choice")

    elif pokemon_type == "Charmander":
        attack_number = int(input("Choose Scratch (1) or Flamethrower (2): "))
        if attack_number == 1:
            print("You missed. Charmander has taken damage.")
            damage_taken = random.randint(20, 50)
            return damage_taken
        elif attack_number == 2:
            print("It was a critical hit! Wombat has fainted!")
            damage_taken = 0
            return damage_taken
        else:
            print("Invalid choice")

    else:
        attack_number = int(input("Choose Vine Whip (1) or Solar Beam (2): "))
        if attack_number == 1:
            print("You missed. Bulbasaur has taken damage.")
            damage_taken = random.randint(20, 50)
            return damage_taken
        elif attack_number == 2:
            print("It was a critical hit! Wombat has fainted!")
            damage_taken = 0
            return damage_taken
        else:
            print("Invalid choice")

def choose_random_pokemon():
    random_pokemon = random.choice(["Eevee", "Horsea", "Squirtle", "Snorlax", "Mewtwo"])
    return random_pokemon

def catch_pokemon(random_pokemon):
    random_number = random.randint(1, 2)
    if random_number == 1:
        print()
        print(f"The {random_pokemon} got away.")
        damage_taken = 100
        return damage_taken
    else:
        print()
        print(f"You caught the wild {random_pokemon}!")
        damage_taken = -50
        return damage_taken

def make_decision(pokemon_type, random_pokemon):
    print()
    print("You encounter a wild Pokemon. Do you want to battle it or try to catch it?")
    print("1. Battle it")
    print("2. Try to catch it")
    decision = int(input("What is your decision (1 or 2): "))
    if decision == 1:
        damage_taken = pokemon_battle(pokemon_type)
        return damage_taken
    elif decision == 2:
        damage_taken = catch_pokemon(random_pokemon)
        return damage_taken
    else:
        print("Invalid choice.")

def manage_health(remaining_health, damage_taken):
    remaining_health = remaining_health - damage_taken
    if remaining_health < 0:
        print(f"Your Pokemon has fainted. Game Over.")
    return remaining_health

def game_end(remaining_health):
    if remaining_health <= 0:
        print("Score: 0")
    elif 0 < remaining_health < 100:
        print("Score: 50")
    elif remaining_health == 100:
        print("Score: 100")
    else:
        print("Score: 150")

player_name, pokemon_type = choose_pokemon()
game_intro(player_name, pokemon_type)
random_pokemon = choose_random_pokemon()
damage_taken = make_decision(pokemon_type, random_pokemon)
remaining_health = manage_health(100, damage_taken) 
game_end(remaining_health)