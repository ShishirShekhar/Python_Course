import random

print("Welcome to Rock, Paper and Scissors")
print("Rules:\n0 is used for Rock\n1 is used for Paper\n2 is used for Scissors")

choice = [0, 1, 2]
score = {"player score":0, "computer score":0}

while score["player score"] < 10 and score["computer score"] < 10:

    computer = random.choice(choice)
    player = int(input("Enter your choice:"))

    if computer == 0:
        if player == 1:
            print(f"Computer choice={computer}\nYou win")
            score["player score"]+=1

        elif player == 2:
            print(f"Computer choice={computer}\nYou lose")
            score["computer score"]+=1

        else:
            print("It's a draw")

    elif computer == 1:
        if player == 0:
            print(f"Computer choice={computer}\nYou lose")
            score["computer score"]+=1

        elif player == 2:
            print(f"Computer choice={computer}\nYou win")
            score["player score"]+=1

        else:
            print("It's a draw")

    else:
        if player == 0:
            print(f"Computer choice={computer}\nYou win")
            score["player score"]+=1

        elif player == 1:
            print(f"Computer choice={computer}\nYou lose")
            score["computer score"]+=1
            
        else:
            print("It's a draw")

    print(score)