# Shopping list using for loop
"""
n = int(input("Enter the number of items: "))
shopping = []

for i in range(n):
    item = input("Enter the item: ")
    shopping.append(item)
    
print(shopping)
"""

# Shopping list using while loop
print("Welcome to shopping list app")
print("Enter q to quit\n")

shop = []
item = input("Enter your shopping item: ")

while item.lower() != 'q':
    shop.append(item)
    item = input("Enter your shopping item: ")

print("\nYour shopping list is ready!!")   
print(shop)
