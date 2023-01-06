from datetime import datetime

curr = datetime.now()
hour = curr.hour

# if 8 <= hour <= 12 :
#     print("Good morning sir")
# elif 12 < hour <= 16 :
#     print("Good afternoon sir")
# elif 16 < hour <= 20 :
#     print("Good Evening sir")
# else:
#     print("Good night sir")

print(curr.strftime("%H::%M::%S::%Y::%m"))
