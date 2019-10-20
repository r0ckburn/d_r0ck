import random
# could also enter "from random import randint"
# and only reference randint in the rand_num variable

player_wins = 0
computer_wins = 0

while player_wins > 2 and computer_wins > 2:
    print(f"Player Score: {player_wins} Computer Score: {computer_wins}")
    print("Rock...")
    print("Paper...")
    print("Scissors...")

    player = input("player, make your move: ").lower()

    rand_num = random.randint(0, 2)
    if rand_num == 0:
        computer = "rock"
    elif rand_num == 1:
        computer = "paper"
    else:
        computer = "scissors"
    print(f"Computer chose {computer}")

    if player == computer:  # this is the most common scenario, and should be first
        print("It's a tie!")
    elif player == "rock":
        if computer == "scissors":
            print("player wins!")
            player_wins += 1
        if computer == "paper":
            print("computer wins!")
            computer_wins += 1
    elif player == "paper":
        if computer == "scissors":
            print("computer wins!")
            computer_wins += 1
        if computer == "rock":
            print("player wins!")
            player_wins += 1
    elif player == "scissors":
        if computer == "rock":
            print("computer wins!")
            computer_wins += 1
        if computer == "paper":
            print("player wins!")
            player_wins += 1
    else:
        print("Please enter a valid move!")
