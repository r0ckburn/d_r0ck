print("Rock...")
print("Paper...")
print("Scissors...")

player1 = input("Player 1, make your move: ")
print("***NO CHEATING!***\n" * 20)
player2 = input("Player 2, make your move: ")

if player1 == player2: # this is the most common scenario, and should be first
    print("It's a tie!")
elif player1 == "rock":
    if player2 == "scissors":
        print("Player 1 wins!")
    if player2 == "paper":
        print("Player 2 wins!")
elif player1 == "paper":
    if player2 == "scissors":
        print("Player 2 wins!")
    if player2 == "rock":
        print("Player 1 wins!")
elif player1 == "scissors":
    if player2 == "rock":
        print("Player 2 wins!")
    if player2 == "paper":
        print("Player 1 wins!")
else:
    print("Something went wrong!")

# another solution:

# p1 = input("Player 1: Choose Rock, Paper or Scissors: ")
# p2 = input("Player 2: Choose Rock, Paper or Scissors: ")

# if p1 == p2:
#     print("Draw")
# elif p1 =="rock" and p2 == "scissors":
#     print("Player 1 wins!")
# elif p1 == "paper" and p2 == "rock":
#     print("Player 1 wins!")
# elif p1 == "scissors" and p2 == "paper":
#     print("Player 1 wins!")
# else:
#     print("Player 2 wins!")

# v1 game:

# if player1 == "rock" and player2 == "scissors":
#     print("Player 1 wins!")
# elif player1 == "rock" and player2 == "paper":
#     print("Player 2 wins!")
# elif player1 == "paper" and player2 == "rock":
#     print("Player 1 wins!")
# elif player1 == "paper" and player2 == "scissors":
#     print("Player 2 wins!")
# elif player1 == "scissors" and player2 == "rock":
#     print("Player 2 wins!")
# elif player1 == "scissors" and player2 == "paper":
#     print("Player 1 wins!")
# elif player1 == player2:
#     print("It's a tie!")
# else:
#     print("Something went wrong!")
