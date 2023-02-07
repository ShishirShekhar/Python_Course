# ask>check>endof quiz>quesseion no>next quesiton
import random
from threading import Timer


class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.q_list = q_list
        random.shuffle(self.q_list)
        self.score = 0

    def still_question(self, result=True):
        if (self.question_number < (len(self.q_list))):
            return True
        return False

    def next_question(self):
        self.question = self.q_list[self.question_number].text
        self.option = self.q_list[self.question_number].option
        random.shuffle(self.option)
        list2 = ["a", "b", "c", "d"]
        self.my_dict = dict(zip(list2, self.option))

        # print(self.option1)
        print(f"{self.question_number+1}: {self.question}?")
        for key in self.my_dict:
            print(f"{key}.{self.my_dict[key]}")

        time_limit = 20
        print(f"You have {time_limit},Seconds to write")
        t = Timer(time_limit, lambda: print("\ntimeout"))
        t.start()

        self.user_answer = input("Your answer: ")
        t.cancel()
        self.question_number += 1

    def check_answer(self):
        answer = self.q_list[self.question_number-1].answer
        if answer == self.my_dict[self.user_answer.lower()]:
            result = True
            self.score += 1
        else:
            result = False

        return result

    def exit(self, money, user_exit='y', result=True):

        if money[self.score] >= 640000:
            print("You have exited with ₹640000.")
            # break/
        elif money[self.score] >= 80000:
            print("You have exited with ₹80000")
            # break
        else:
            print(f"You have exited with {money[self.score]}")
