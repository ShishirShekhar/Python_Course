from question_model import Question
from data import my_dict, money_list
from quiz_brain import QuizBrain
print("Welcome to KBC: ")
# user_name = input("Enter your name: ")

question_bank = []

for question in my_dict:
    question_text = question["question"]
    question_answer = question["answer"]
    question_option = question["option"]
    new_question = Question(question_text, question_answer, question_option)
    question_bank.append(new_question)

# print(question_bank)

kbc = QuizBrain(question_bank)

while kbc.still_question():
    kbc.next_question()
    result = kbc.check_answer()
    print(result)
    if result:
        print(
            f"Congrats your answer is correct!\nYour current score is {kbc.score}/14.\nCurrent Money: {money_list[kbc.score]}\n\n")
        user_exit = input("Do you want to exit here? y/n: ")

        if user_exit.lower() == 'y':
            kbc.exit(money_list, user_exit)
            break

    else:
        print(
            f"oops! your answer is wrong.\nYou have completed the game\nYou lost the game.\nYour final score is {kbc.score}/14.")
        kbc.exit(money_list)
        break
if kbc.score == 14:
    print("Congratulations u are a Crorepati now!")
