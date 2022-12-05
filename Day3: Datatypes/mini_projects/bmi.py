# BMI: Body mass index
# bmi = mass / height * height
# mass in kg, height in meters

mass = eval(input("Enter your mass: "))
height = eval(input("Enter your height: "))

bmi = mass/height**2
print("Your body mass index is:", bmi)
