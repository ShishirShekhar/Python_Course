import random

score_user = 0
score_computer = 0
to_continue = True
while to_continue:

    print("Welcome to rock,paper,scissors game")
    move_player = input(
        "What do you choose?Type 0 for Rock,1 for paper or 2 for scissors.")
    move_1 = int(move_player)
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
    player_move = [rock, paper, scissors]
    if move_1 <= 2 and move_1 >= 0:
        player_move_1 = player_move[move_1]
        print(f"You have chosen {player_move_1}")
        if move_1 == 0 or 1 or 2:
            computer_move = [rock, paper, scissors]
            random_number = random.randint(0, 2)
            move = computer_move[random_number]
            print(f"Computer chose {move}")

            if move_1 == random_number:
                print("The game is a Draw")
            if move_1 == 0:
                if move == paper:
                    print("You lose")
                    score_computer += 1
                elif move == scissors:
                    print("You win")
                    score_user += 1

            if move_1 == 1:
                if move == rock:
                    print("You win")
                    score_user += 1
                elif move == scissors:
                    print("You lose")
                    score_computer += 1
            if move_1 == 2:
                if move == rock:
                    print("You lose")
                    score_computer += 1
                elif move == paper:
                    print("you win")
                score_user += 1
        print(f"Your score: {score_user}\nComputer score {score_computer}")

    else:
        print("you have chosen invalid number you lose.")
    if score_computer < 10 and score_user < 10:
        to_continue = True
    else:
        to_continue = False
