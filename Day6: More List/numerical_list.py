# Class
# sum of two list
num1 = [1, 2, 3, 4, 5]
num2 = [6, 7, 8, 9, 10]
result = []

for i in range(len(num1)):
    result.append(num1[i] + num2[i])
    
print(result)

# Task 1

lst1 = [True, False, True, False, True]
lst2 = [False, False, False, True, True]
and_result = []
or_result = []

for i in range(len(lst1)):
    and_result.append(lst1[i] and lst2[i])
    or_result.append(lst1[i] or lst2[i])

print(and_result)
print(or_result)

# Task 2
# Write a program to find common elements in two lists.
# Find intersection of two lists.
