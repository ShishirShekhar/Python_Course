num = int(input("Enter a number: "))

match num:
    case 1:
        print("The number is good number")
    case 2:
        print("This is a great number")
    case _ if num == 10:
        print("This is a special number")
    case _:
        print("Other number")
