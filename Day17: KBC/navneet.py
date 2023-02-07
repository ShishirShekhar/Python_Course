import time
q1 = """ Who is considered as the father of python language?
a. Guido van Rossum
b. Dennis MacAlistair Ritchie
c. Bjarne Stroustrup
d. James Gosling
"""

q2 = """What is the output of the following expression 8*2**1?
a. 16
b. 64
c. 36
d. 72
"""

q3 = """ What is the output of the following code?

var1 = 1
var2 = 2
var3 = "3"

print(var1 + var2 + var3)

 a. 6
 b. 33
 c. 123
 d. Error, mixing operators between numbers and strings are not supported
 """

q4 = """
A string is immutable in Python?

Every time when we modify the string, Python Always create a new String and assign a new string to that variable.

a. True
b. False
"""

q5 = """What is a correct syntax to output "Hello World" in Python?
a. printf("Hello World")
b. print("Hello World")
c. p("Hello World")
d. echo("Hello World")

"""

#Here values are the correct options of the questions.

questions={
    q1: "a",
    q2: "a",
    q3: "b",
    q4: "a",
    q5: "b",
}

name=(input("Enter your name:"))
print("Hello",name,"Welcome to KBC")
time.sleep(1)
print("Here are some basic rules of our game:\n 1. Every correct answer will boost your score by 1 point. \n 2. Every wrong answer will result in deduction of 1 point and game will be terminated. \n 3. If you don't know the answer you can quit the game and your final score will be counted.")
time.sleep(2)
print("Let's start the game. Best of luck!!")
time.sleep(1)
score=0
number=1
for i in questions:
    print(f"Our {number} question is:")
    time.sleep(1)
    print(i)
    time.sleep(1)
    flag1=input("Do you want to quit the quiz (yes/no): ")
    if flag1.lower()=="yes":
        break
    else:
        answer=input("Enter your answer(a/b/c/d): ")
        if answer.lower()==questions[i]:
            print("Correct answer!! Keep going...")
            score+=1
            number+=1
            time.sleep(1)
        else:
            print("Wrong answer")
            score-=1
            break

time.sleep(2)
print("Counting your final score please wait...")
time.sleep(2)
print("Your final score is",score)