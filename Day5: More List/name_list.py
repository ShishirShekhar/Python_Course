first_name = []
last_name = []
full_name = []
n = 6

for _ in range(n):
    first = input("enter first name:")
    last = input("enter last name:")
    
    first_name.append(first)
    last_name.append(last)
    
    full_name.append(first + " " + last)
    
for i in range(n):
    print(full_name[i])
