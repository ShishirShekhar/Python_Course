import random

score_user = 0
score_computer = 0
to_continue = True
print("Welcome to rock,paper,scissors game")
rock = '''
        ___
    ---'   __)
          (___)
          (___)
          (__)
    ---._(__)
    '''

scissors = '''
        ___
    ---'   _________)
              ________)
              ___)
             ___)
    ---.____)
    '''

paper = '''
        _____)
    ---'   _________)
              _______)
           _________)
          (______)
    ---.______)
    '''


def result(user_move, computer_move):
    result = ""

    if (user_move == 0 and computer_move == 2):
        result = "User wins"

    elif (computer_move == 0 and user_move == 2):
        result = "User lose"

    elif (user_move >= 3 and computer_move < 0):

        result = "invalid number You lose"

    elif (computer_move > user_move):

        result = "User lose"

    elif (user_move > computer_move):
        result = "User wins"

    elif (computer_move == user_move):
        result = "Draw"

    return result


while to_continue:

    move_player = input(
        "What do you choose?Type 0 for Rock,1 for paper or 2 for scissors.")
    move_1 = int(move_player)

    player_move = [rock, paper, scissors]
    if move_1 <= 2 and move_1 >= 0:
        player_move_1 = player_move[move_1]
        print(f"You have chosen {player_move_1}")

        computer_move = [rock, paper, scissors]
        random_number = random.randint(0, 2)
        move = computer_move[random_number]
        print(f"Computer chose {move}")

        res = result(move_1, random_number)
        print(res)
        if res == "User wins":
            score_user += 1
        elif res in ("User lose", "invalid number You lose"):
            score_computer += 1
        else:
            pass

    else:
        print("invalid number You lose")
        score_computer += 1

    print("user score", score_user)
    print("computer score", score_computer)

    if score_computer < 10 and score_user < 10:
        to_continue = True
    else:
        to_continue = False
