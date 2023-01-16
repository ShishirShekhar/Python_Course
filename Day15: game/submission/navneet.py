import random
import time

Choice=['Rock','Paper','Scissors']
while True:
    print('Welcome to Rock Paper Scissors game :)')
    time.sleep(1)
    yourwin,computerwin=0,0

    while yourwin!=10 and computerwin!=10:
        print('Options are :-')
        time.sleep(1)
        print('Rock','Paper','Scissors',sep='\n')
        your_choice=input('Please select an option:')
        time.sleep(1)

        if your_choice.title()=='Rock':
            print('You have selected Rock')
        elif your_choice.title()=='Paper':
            print('You have selected Paper')
        elif your_choice.title()=='Scissors':
            print('You have selected Scissors')
        else:
            print('Please select an valid option')
            break

        print('Computer is selecting...')
        time.sleep(1)
        computer_choice=random.choice(Choice)
        print(f'Computer has selected {computer_choice}')
        time.sleep(2)

        if your_choice.title()==computer_choice:
            yourwin+=1
            computerwin+=1
            print('This round is drawn')
            print(f'Your score is {yourwin}')
            print(f'Computer score is {computerwin}')
            time.sleep(2)
        elif (your_choice.title()=='Paper' and computer_choice=='Rock') or (your_choice.title()=='Scissors' and computer_choice=='Paper') or (your_choice.title()=='Rock' and computer_choice=='Scissors'):
            yourwin+=1
            print('You win this round')
            print(f'Your score is {yourwin}')
            time.sleep(2)
        else:
            computerwin+=1
            print('Computer win this round')
            print(f'Computer score is {computerwin}')
            time.sleep(2)
 
    print('Game-Over','Final Results are here:-',sep='\n')
    time.sleep(1)

    if yourwin>computerwin:
        print(f'Your score is {yourwin}')
        time.sleep(1)
        print(f'Computer score is {computerwin}')
        time.sleep(1)
        print('Congrats you are the winner!!')
        time.sleep(2)
    elif yourwin==computerwin:
        print(f'Your score is {yourwin}')
        time.sleep(1)
        print(f'Computer score is {computerwin}')
        time.sleep(1)
        print("Seems like it's an tie")
        time.sleep(2)
    else:
        print(f'Your score is {yourwin}')
        time.sleep(1)
        print(f'Computer score is {computerwin}')
        time.sleep(1)
        print('Better luck next time!!')
        time.sleep(1)

    user_choice = input('Do you want to play again??(Yes/Exit)')

    if user_choice.lower() == 'yes':
        print('Game is restarting...')
        time.sleep(2)
        continue
    else:
        print('Good-bye!!')
        break