scoreboard = {}

print("Welcome to admin command mode!!")
print("Now you can modify the scoreboard!")
print("Enter 'q' to exit any time")

name = input("\nEnter the name of player: ")
score = 0
p_rem = 'y'

while (name != 'q' and score != 'q' and p_rem != 'q'):
    score = input(f"Enter {name}'s score: ")
    score = int(score)
    scoreboard[name] = score
    print("\nThe current scoreboard: ")
    print(scoreboard)

    modify = input("\nDo you want to modify someone's score(y/n)? ")
    if (modify == "y"):
        name = input("Enter player name you want to modify: ")
        score = int(input("Current score of the player: "))
        
        scoreboard[name] = score

    print("\nThe current scoreboard: ")
    print(scoreboard)

    p_rem = input("\nDo you want to remove any player(y/n)? ")
    if (p_rem == "y"):
        name = input("Enter player name you want to remove: ")
        del scoreboard[name]
        
    print("\nThe current scoreboard: ")
    print(scoreboard)
    
    name = input("\nEnter the name of player: ")
    score = input(f"Enter {name}'s score: ")
