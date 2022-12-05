# 2x**2 + 4x + 5

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

root1 = (- b + (b ** 2 - 4 * a * c) ** (1/2)) / (2 * a)
root2 = (- b - (b ** 2 - 4 * a * c) ** (1/2)) / (2 * a)
print("Roots are:", root1, root2)
