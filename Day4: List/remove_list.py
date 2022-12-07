# Create a empty list of cars
# Use append to add value in the list
# Print all the value with a msg, I like cars[i]

cars = []

cars.append("Audi")
cars.append("Mercedes-Benz")
cars.append("BMW")
cars.append("Jaguar")

# del cars[3]
# print(cars)

# cars.pop()
# print(cars)

# Pop the last value of the cars list and print i would not like to drive var
car = cars.pop()
print("I would not like to drive", car)
print(cars)

cars.remove("BMW")
print(cars)
