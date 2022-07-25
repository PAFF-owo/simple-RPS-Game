from random import randint
po = ["R", "P", "S"]

opponent = po[randint(0, 2)]
player = 0

while player == 0:
    player = input("R, P, S? \n Enter H for help: ")
    if player == opponent:
        print("Tie")
    elif player == "R":
        if opponent == "P":
            print("You lost", opponent, "Defeats", player)
        else:
            print("You win", player, "Defeats", opponent)
    elif player == "S":
        if opponent == "R":
            print("You lost", opponent, "Defeats", player)
        else:
            print("You win", player, "Defeats", opponent)
    elif player == "P":
        if opponent == "S":
            print("You lost", opponent, "Defeats", player)
        else:
            print("You win", player, "Defeats", opponent)
    else:
        print("Its not right check your Input")
    if player == "H":
        print("""R is For Rock 
        P is for Paper
        S is for Scissors""")

    player = 0
    opponent = po[randint(0, 2)]
