from random import randint
po = ["Rock", "Paper", "Scissor", "Shotgun"]

opponent = po[randint(0, 2)]
player = 0

while player == 0:
    player = input("Rock, Paper, Scissor?\nEnter H for help\nEnter Your move:  ")

    if player == opponent:
        print("Tie")
    elif player == "Rock":
        if opponent == "Paper":
            print("You lost", opponent, "Defeats", player)
        else:
            print("You win", player, "Defeats", opponent)
    elif player == "Scissor":
        if opponent == "Rock":
            print("You lost", opponent, "Defeats", player)
        else:
            print("You win", player, "Defeats", opponent)
    elif player == "Paper":
        if opponent == "Scissor":
            print("You lost", opponent, "Defeats", player)
        else:
            print("You win", player, "Defeats", opponent)
    if player == "H":
        print("Rules:\nRock defeats Scissor\nPaper Defeats Rock\nScissor Defeats Paper")
    else:
        print("Its not right check your Input")
    input("Press Enter to continue")

    print("\n")




    player = 0
    opponent = po[randint(0, 2)]
