print("Enter your operation:")
user_input = input()
num1, op, num2 = user_input.split(" ")
num1 = eval(num1)
num2 = eval(num2)
result = 0

# if-elif-else 
if op == "+":
    result = num1 + num2
elif op == "-":
    result = num1 - num2
elif op == "*":
    result = num1 * num2
elif op == "/":
    result = num1 / num2
else:
    result = "Operation cann't be processed"


print(f"{user_input} = {result}")
