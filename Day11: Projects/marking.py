grade=["A","B","C","D","E"]

num=int(input("number enter: "))
mark=10-(num//10)-1
if mark>len(grade):
    print("F")
else:
    print(grade[mark])
