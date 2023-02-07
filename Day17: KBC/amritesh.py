kbc = {
    1: {"What is the capital of India ?": ["(A) New Delhi", "(B) Mumbai", "(C) Chennai", "(D) Bangalore"],
        "Answer": "A"},
    2: {"Who is the prime minister of India ?": ["(A) Rajnath Singh", "(B) Narendra Modi", "(C) S.Jaishankar", "(D) Nirmala Sitharaman"],
        "Answer": "B"},
    3: {"What is the capital of U.S.A ?": ["(A) Seattle", "(B) Washington D.C", "(C) New York", "(D) Philadelphia"],
        "Answer": "B"}
}
print("Hi! Welcome to KBC")
score = 0
level = 1
while level < 4:
    quest = list(kbc[level].keys())
    options = list(kbc[level].values())
    print("\nQuestion", level, ":")
    print(quest[0])
    for opt in options[0]:
        print(opt)
    if input("Your Answer: ").upper() == kbc[level]["Answer"]:
        print("Correct Answer !")
        score += 1
    else:
        print("Wrong Answer !, Better luck next time")
        print("Your score is:", score)
        break
    print("Your score is:", score)
    level += 1
else:
    print("You won the GAME !\nThank You! for Playing")
