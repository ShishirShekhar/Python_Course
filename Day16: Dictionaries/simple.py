alien_0 = {
    "color": "green",
    "points": 5,
    "hp": 100,
    "level": 1
}

score = 0
print("Your score is", score)

hit = int(input("Hit or not: "))
if (hit):
    score += alien_0["points"]
    
print("Your score is", score)


