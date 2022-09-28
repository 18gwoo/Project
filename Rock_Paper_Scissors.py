import random
#Can be improved by putting all the print statements at bottom instead of the if statements. Instead assign variables to each if statement and use these variables to make print statements
while True:

    choices = ["rock","paper","scissors"]
    player = None
    computer = random.choice(choices)

    while player not in choices:
        print("Welcome to rock, paper, scissors.", end = " ")
        player = input("What would you like to picK: Rock, Paper or Scissors?: ").lower()

    print()

    if computer == player:
        print("Opponent has picked " + computer)
        print("Player has picked " + player)
        print("Result is a tie.")
    elif player == "scissors":
        if computer == "rock":
            print("Opponent has picked " + computer)
            print("Player has picked " + player)
            print("Rock beats scissors. Opponent wins.")
        else:
            print("Opponent has picked " + computer)
            print("Player has picked " + player)
            print("Scissors beats paper. Player wins")
    elif player == "rock":
        if computer == "paper":
            print("Opponent has picked " + computer)
            print("Player has picked " + player)
            print("Paper covers rock. Opponent wins")
        else:
            print("Opponent has picked " + computer)
            print("Player has picked " + player)
            print("Rock beats scissors. Player wins")
    elif player == "paper":
        if computer == "scissors":
            print("Opponent has picked " + computer)
            print("Player has picked " + player)
            print("Scissors cuts paper. Opponent wins")
        else:
            print("Opponent has picked " + computer)
            print("Player has picked " + player)
            print("Paper covers rock. Player wins")
    print()
    again = input("Play again? yes/no: ").lower()
    print()
    if not again == "yes":
        break
