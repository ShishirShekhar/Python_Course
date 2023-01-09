# Flag
"""
print("Welcome to shopping list app")
print("Enter q to quit\n")

shop = []
flag = True

while flag:
    item = input("Enter your shopping item: ")
    if item.lower() != 'q':
        shop.append(item)
    else:
        flag = False

print("\nYour shopping list is ready!!")   
print(shop)
"""

# break

print("Welcome to shopping list app")
print("Enter q to quit\n")

shop = []

while True:
    item = input("Enter your shopping item: ")
    if item.lower() != 'q':
        shop.append(item)
    else:
        break

print("\nYour shopping list is ready!!")   
print(shop)
