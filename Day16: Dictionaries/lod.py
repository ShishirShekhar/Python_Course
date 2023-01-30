alien_0 = {
    "color": "green",
    "points": 5,
    "hp": 100,
    "level": 1
}

alien_1 = {
    "color": "yellow",
    "points": 10,
    "hp": 150,
    "level": 2
}

alien_2 = {
    "color": "orange",
    "points": 20,
    "hp": 200,
    "level": 3
}

aliens = [alien_0, alien_1, alien_2]

level = int(input("Enter the level you want to play(1/2/3): "))
level -= 1

print("\nDetails of alien you are going to face: ")
for key, value in aliens[level].items():
    print(f"{key}: {value}")
