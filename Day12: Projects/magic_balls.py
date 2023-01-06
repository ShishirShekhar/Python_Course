import random
import time

ans_list = ['it is certain.', 'As I see it, yes.', 
       'Reply hazy, try again.', 'Don\'t count on it.', 
       'It is decidedly so.', ' Most likely.', 
       'Ask again later.', 'My reply is no.'
       ]

print("Welcome to the Almighty Magic Ball")

user_input = input("Ask your question: ")
ans = random.choice(ans_list)

print("The magic ball is thinking...")
time.sleep(3)
print(ans)

# By Abhishek
