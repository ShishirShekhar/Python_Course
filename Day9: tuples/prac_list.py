# Task 1:
"""
Create a list for pizza menu and print it like this
1 some pizza name
2 some other pizza name
3 some other other pizza name
"""

menu = ["Greek Pizza", "Neapolitan Pizza", "Cheese pizza",
        "Chicago pizza", "New york style pizza"]

print("Welcome to pizza hub\n")
print("*"*10, "Menu", "*"*10)

for index, value in enumerate(menu, 1):
    print(index, "\t", value)
    
"""
enu = [(0, "Greek Pizza"), (1, "Neapolitan Pizza"), 
 (2, "Cheese pizza"), (3, "Cheese pizza")]
"""

# Task 2
"""
Take input from user for the order and print the ordered pizza
"""
order = int(input("Enter the pizza number: "))
pizza = menu[order - 1]


# Task 3
"""
Create a second list for available pizzas,
check if order is in available pizzas, if yes, print order
"""

available = ["Greek Pizza", "Neapolitan Pizza"]
serve = pizza in available and pizza or "Not Available"

print(serve)
