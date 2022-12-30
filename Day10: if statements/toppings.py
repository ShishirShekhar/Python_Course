requested_toppings = [input("Enter your topping request: ") for _ in range(int(input("Enter the number of toppings: ")))]
available_toppings = ["mushroom", "onion", "pepperonis", "cheese"]

if requested_toppings:
    print("Preparing your pizza.....")
    for requested_topping in requested_toppings:
        if requested_topping == "":
            print("Invalid")
        elif requested_topping in available_toppings:
            print(f"Adding {requested_topping}....")
        else:
            print(f"{requested_topping} is not available")

    print("\nYour pizza is ready!")
else:
    print("You need to select a topping")
