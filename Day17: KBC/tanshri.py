import time

print("---------------")
print("Welcome to KBC")
print("--------------")
time.sleep(5)
print("You will be displayed a question and you have to choose the option among the four options")
print("------------")
time.sleep(5)
print("So Lets start")

ques = {"What is the name of current president of India": 
        ["Draupadi Murmu", "Pranav Mukhrjee", "Pratibha Patil", "Rajendra Prasad"], 
        "How many sessions of parliament are conducted?": ["Three", "Two", "One", "Four"], "Which state of India is largest producer of jute?": ["West Bengal", "Uttar Pradesh", "Odissa", "Jharkhand"],
        "What is the name of Indian author who get shot in London for his controversial remarks on a religion": ["Salman Rushdie", "Chetan Bhagat", "Mark Manson", "Ankur Warikoo"], "When USA celebrate their independence day?": ["4 May", "5 May", "4 June", "5 June"], "Which of the following gods is also known as Gauri Nandan": ["Shiv", "Vishnu", "Braham", "Krishna"]}

option = "A"
score = 0
question = 0
while option == "A":
    print(f"So question {question+1}")
    print(list(ques.keys())[question])
    print(list(ques.values())[question])
    option = input("Enter your answer")
    if option == "A":
        score += 1
    time.sleep(5)
    question += 1

print(score)
