num1, op, num2 = input().split(" ")
num1 = eval(num1)
num2 = eval(num2)
result = num1

# Add your code here
match op:
    case "+":
        result = num1+num2
    case "-":
        result = num1-num2
    case "*":
        result = num1*num2
    case "/":
        result = num1/num2
    case _:
        result = "This operation cannot be performed!!"

print(result)
