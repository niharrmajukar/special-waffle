import random

choice = {-1: "stone", 0: "paper", 1: "scissors"}

you = int(input("Enter your choice (-1 stone, 0 paper, 1 scissors): "))

computer = random.choice([-1, 0, 1])

print("Computer chose:", choice[computer])

if computer == you:
    print("It's a draw")

elif computer == 1 and you == 0:
    print("Computer wins")
elif computer == 1 and you == -1:
    print("You win")
elif computer == 0 and you == 1:
    print("You win")
elif computer == 0 and you == -1:
    print("Computer wins")
elif computer == -1 and you == 1:
    print("Computer wins")
elif computer == -1 and you == 0:
    print("You win")
else:
    print("Invalid input")
