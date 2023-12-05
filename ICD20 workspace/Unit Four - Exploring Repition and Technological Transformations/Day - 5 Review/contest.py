

def calculate_wins():
    game_1 = input("First game result: ")
    game_2 = input("Second game result: ")
    game_3 = input("Thrid game result: ")
    game_4 = input("Fourth game result: ")
    game_5 = input("Fith game result: ")
    game_6 = input("Sixth game result: ")
    wins = 0
    if game_1 == "W":
        wins += 1

    if game_2 == "W":
        wins += 1

    if game_3 == "W":
        wins += 1

    if game_4 == "W":
        wins += 1

    if game_5 == "W":
        wins += 1

    if game_6 == "W":
        wins += 1
    return wins

def aaa_(wins):
    if wins == 5:
        print("1")
    if wins == 6:
        print("1")
    elif wins == 3:
        print("2")
    elif wins == 4:
        print("2")
    elif wins == 1:
        print("3")
    elif wins == 2:
        print("3")
    else:
        print("-1")
wins = calculate_wins()
aaa_(wins)