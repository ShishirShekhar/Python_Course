scoreboard = {}

n = int(input("Enter the number of players: "))

for _ in range(n):
    name = input("\nEnter the name of player: ")
    score = int(input(f"Enter {name}'s score: "))
    
    scoreboard[name] = score

print("\nThe current scoreboard: ")
print(scoreboard)

modify = input("\nDo you want to modify someone's score(y/n)? ")
if (modify == "y"):
    p_name = input("Enter player name you want to modify: ")
    curr_score = int(input("Current score of the player: "))
    
    scoreboard[p_name] = curr_score

print("\nThe current scoreboard: ")
print(scoreboard)

p_rem = input("\nDo you want to remove any player(y/n)? ")
if (p_rem == "y"):
    p_name = input("Enter player name you want to remove: ")
    del scoreboard[p_name]
    
print("\nThe current scoreboard: ")
print(scoreboard)
