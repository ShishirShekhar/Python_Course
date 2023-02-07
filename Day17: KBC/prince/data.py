import random

questions = ["Who is The Prime Minister of India",
             "In Which Country Area 51 is Located",
             "Which one is the largest Continent in the world",
             "What is the Latest Version of Windows Since 2019",
             "Which One of These Is not a Software Company",
             "How Many MB Makes 1 GB",
             "Facebook Was Firstly Developed By",
             "Founder of Apple is",
             "_________ is one of The Founder of Google",

             "BIGG BOSS season 13 Starts in ____ & ends in _____",
             "Apple's Laptop is Also Known as",
             "First Apple Computer is Known as",
             "Joystick is used For",
             "____________ is used to Encrypt Drives in Computer"]

answer = ["Narendra Modi",
          "United States",
          "Asia",
          "Windows 11",
          "Honda",
          "1024",
          "Mark Zuckenberg",
          "Steve Jobs",
          "Larry Page",
          "2019 - 2020",
          "Macbook",
          "Mactonish",
          "Playing Games",
          "Bitlocker"]

wronganswers = [["Amit Shah",
                 "Aditya Nath Yogi",
                 "Azhar Ansari"],
                ["India", "Africa", "Iraq"],
                ["South Africa", "North America", "Europe"],
                ["Windows 7", "Windows 8", "Windows 10"],
                ["Oracle", "Microsoft", "Google"],
                ["10024", "1004", "2024"],
                [
                    "Bill Gates", "Larry Page", "Azhar Ansari"],
                ["Azhar Ansari", "Charles Babbage", "Sundar Pichai"],
                [
    "Larry Hensberg", "Sunder Pichai", "Bill Gates"],
    ["2020 - 2021", "Not Starts Now", "2018 - 2019"],
    ["ThinBook", "Notebook", "ChromeBook"],
    ["Apple v.1", "Apple Computer", "Appbook"],
    [
        "Giving output command", "Shutting down Computer", "Log off Computer"],
    ["KeyGuard", "Windows Secure", "No Software like this"]
]

wronganswers1 = [["Amit Shah",
                 "Aditya Nath Yogi",
                  "Azhar Ansari"],
                 ["India", "Africa", "Iraq"],
                 ["South Africa", "North America", "Europe"],
                 ["Windows 7", "Windows 8", "Windows 10"],
                 ["Oracle", "Microsoft", "Google"],
                 ["10024", "1004", "2024"],
                 [
    "Bill Gates", "Larry Page", "Azhar Ansari"],
    ["Azhar Ansari", "Charles Babbage", "Sundar Pichai"],
    [
    "Larry Hensberg", "Sunder Pichai", "Bill Gates"],
    ["2020 - 2021", "Not Starts Now", "2018 - 2019"],
    ["ThinBook", "Notebook", "ChromeBook"],
    ["Apple v.1", "Apple Computer", "Appbook"],
    [
        "Giving output command", "Shutting down Computer", "Log off Computer"],
    ["KeyGuard", "Windows Secure", "No Software like this"]
]

my_dict = []
for i in range(len(questions)):
    wronganswers[i].append(answer[i])
    dict2 = {"question": questions[i],
             "answer": answer[i],
             "option": wronganswers[i],
             "fifty": [answer[i], random.choice(wronganswers1[i])],
             }
    my_dict.append(dict2)

# print(my_dict)
# data = my_dict
# print(data)
money_list = [0, 1000, 2000, 3000, 5000, 10000, 40000, 80000,
              160000, 320000, 640000, 1500000, 3000000, 5000000, 10000000]
