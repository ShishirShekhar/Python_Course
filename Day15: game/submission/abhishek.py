import random
import time

f = open("scores.txt", "wt")


def leaderboard():
    global scores, yes_msg, no_msg, curr_user
    print("User Name \t Games Played\t Total Wins \tTotal Losses\t"
          " Win Percentage \tHighest Winning Streak \tCurrent Winning Streak")
    for i in scores:
        for j in i:
            print(j, end="\t")
    print("(1) Return to Main Menu\n(2) Reset Leaderboard\n(3) Create new user")
    choice1 = int(input("PLease input the corresponding number to your option: "))
    if choice1 == 1:
        main_menu()
    elif choice1 == 2:
        choice2 = input("Reset Leaderboard ? (Y/N)")
        if choice2 in yes_msg:
            scores = []
            print("Whoosh!, Time for a fresh start")
        elif choice2 in no_msg:
            print("Phew, glad you changed your mind")
        else:
            print("Invalid Choice")
            leaderboard()
    elif choice1 == 3:
        user_name = input("Please enter user name: ")
        scores.append([user_name, 0, 0, 0, 0, 0, 0])
        curr_user = user_name
        print(f"New User Successfully Created - {user_name}")
    choice2 = input("Reset Leaderboard ? (Y/N)")
    if choice2 in yes_msg:
        scores = []
        print("Whoosh!, Time for a fresh start")
    elif choice2 in no_msg:
        print("Phew, glad you changed your mind")
    else:
        print("Invalid Choice")
        leaderboard()


def user_scores():
    global user_score
    print("You score!")
    user_score += 1


def comp_scores():
    global comp_score
    print("Rocky scores!")
    comp_score += 1


def game():
    global scores, yes_msg, no_msg, user_score, comp_score, winner
    user_name = input("Please enter your name: ")
    if user_name in scores:
        print(f"Welcome {user_name}/n")
    else:
        new_user = input("User not found, would you like to create a new user? (Y/N)")
        if new_user in yes_msg:
            scores.append([user_name, 0, 0, 0, 0, 0, 0])
            print(f"New User Successfully Created - {user_name}")
        elif new_user in no_msg:
            exit("Seems like you don't want to play, well, please come back when you change your mind")

    choices = ["rock", "paper", "scissor"]
    print("Waking up the bot...")
    time.sleep(1)
    print("Explaining the rules to the bot")
    time.sleep(1)
    print("Repeatedly telling the bot not to choose rock every time...")
    time.sleep(1)
    print("The bot is here, it'll be fun to watch\n")
    print("Hello, I am Rocky, and I'll help you in losing this game :)")
    print("Let's get started ")
    score_limit = int(input("So, how many points to win"))
    user_score = 0
    comp_score = 0
    while user_score < score_limit and comp_score < score_limit:
        user_choice = input("Rock/Paper/Scissor: ")
        user_choice = user_choice.lower()
        while user_choice not in choices:
            print("Invalid Input")
            user_choice = input("Rock/Paper/Scissor: ")

        comp_choice = random.choice(choices)
        print("Rocky chooses:", comp_choice.title())
        print()
        if user_choice == comp_choice:
            print("As they say, great minds think alike. It's a draw")

        elif user_choice == "rock":
            if comp_choice == "paper":
                print("Paper enfolds Rock")
                comp_scores()
            else:
                print("Rock smashes Scissors")
                user_scores()

        elif user_choice == "paper":
            if comp_choice == "rock":
                print("Paper enfolds Rock")
                user_scores()
            else:
                print("Scissor shreds Paper")
                comp_scores()

        elif user_choice == "scissor":
            if comp_choice == "paper":
                print("Scissor shreds Paper")
                user_scores()
            else:
                print("Rock smashes Scissors")
                comp_scores()
        print(f"Your score: {user_score}")
        print(f"Rocky's score: {comp_score}")

    if user_score > comp_score:
        print("Rocky: What? You are definitely cheating, I am going to sleep.\n")
        print("Congrats, you won!!")
        winner = curr_user
    else:
        print("Haha, you lost, seems like robot supremacy is not a distant thing, I'll go rest for now\n")
        print("Imagine losing to a bot, oh wait, you don't have to imagine, lol")
        winner = "Rocky"
    print("(1)Return to Main Menu\n (2) See the Leaderboard\n (3) Exit the program")
    final_choice = int(input("What would you like to do? (1/2/3) "))
    if final_choice == 1:
        main_menu()
    elif final_choice == 2:
        leaderboard()
    elif final_choice == 3:
        exit_msg()
    else:
        print("Invalid Choice")
        time.sleep(1)
        print("Returning to Main Menu")
        main_menu()


def exit_msg():
    exit("Thanks for playing, come back again to win and be at the top")


def main_menu():
    menu_choice = int(input("Please select between 1, 2 and 3: "))
    if menu_choice == 1:
        game()
    elif menu_choice == 2:
        leaderboard()
    elif menu_choice == 3:
        exit_msg()
    else:
        print("Invalid Choice")


def final():
    global winner, f


yes_msg = ["yes", "y"]
no_msg = ["no", "n"]
scores = []
print()
print("Welcome to Rock Paper Scissor".center(100, "-"))
print("\nThe childhood game we all love, brought to you in digital form\n")
print("Currently we only support single player mode, but still you can compete with your friends on the leaderboard.\n")
print("What would you like to do?", "(1) Play the game", "(2) See the leaderboard", "(3) Exit the game\n", sep="\n")
main_menu()
f.close()
