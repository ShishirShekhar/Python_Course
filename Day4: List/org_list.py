marks = [43, 12, 21, 46, 65]

# Sort permanently
# marks.sort()
# marks.sort(reverse=True)

# print('The highest marks obtained is', marks[0])
# print("The lowest marks obtained is", marks[-1])

# Temporary sort
print(sorted(marks))
print(marks)

print('The highest marks obtained is', sorted(marks)[-1])
print("The lowest marks obtained is", sorted(marks)[0])
print(marks)

# Reverse
marks.reverse()
print(marks)
marks.reverse()
print(marks)

# length
l = len(marks)
print(l)

# Error
print(marks[5])
