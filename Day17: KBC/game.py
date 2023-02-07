game = {
    0: {
        "question": "What is the mass of the electron",
        "options": ["8.85*10^-31", "6.66*10-27", "1.6*10-19", "9.1*10-31"],
        "answer": "9.1*10-31"
    }
}

print(game[0]["question"])
for i, option in enumerate(game[0]["options"], 1):
    print(f"{i}: {option}")
    
ans = int(input("Enter your option: "))

if (game[0]["options"][ans-1] == game[0]["answer"]):
    print("correct")
else:
    print("incorrect")
