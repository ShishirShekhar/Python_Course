import random

def play_rps():
    options = ['rock', 'paper', 'scissors']
    score = [0, 0]
    while True:
        player_choice = input('rock, paper, or scissors (or "q" to quit): ')

        if player_choice == 'q':
            break
        
        if player_choice not in options:
            print('Invalid choice')
            continue

        pc_choice = random.choice(options)
        print('Computer choses:', pc_choice)
        if player_choice == pc_choice:
            print('Tie')
        elif (player_choice == '0' and pc_choice == '3') or \
            (player_choice == '1' and pc_choice == '1') or \
            (player_choice == '2' and pc_choice == '2'):
            print('You win')
            score[0] += 1
        else:
            print('You lose')
            score[1] += 1
        
        print(f'Score: {score[0]} - {score[1]}')
    
    print(f'Final Score: {score[0]} - {score[1]}')

play_rps()
