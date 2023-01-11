import random
choices = ["rock","paper","scissors"]
user_points = 0
pc_points = 0

while pc_points < 10 and user_points < 10 :
    pick = input("enter your choice from rock, paper, scissors: ")
    pc = random.choice(choices)
    
    if pick == pc:
        print("it's a draw")
    elif pick == "rock" and pc == "paper":
        print("pc won the round")
        pc_points += 1
    elif pick == "rock" and pc == "scissors": 
        print("user won the round")
        user_points += 1 
    elif pick == "paper" and pc == "rock" :
        print("user won the round") 
        user_points += 1  
    elif pick == "paper" and pc == "scissors" :
        print("pc won the round")
        pc_points += 1 
    elif pick == "scissors" and pc == "rock" :
        print("pc won the round")
        pc_points += 1 
    elif pick == "scissors" and pc == "paper" :
        print("user won the round")
        user_points += 1
        
    print("user points =",user_points,"pc_points =",pc_points)

if pc_points == 10 :
    print("pc has won the match")
elif user_points == 10 :
    print("user has won the match")
