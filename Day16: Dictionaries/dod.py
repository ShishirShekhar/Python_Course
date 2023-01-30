class_marks = {
    "priyanshu": {
        "maths": 10,
        "english": 20,
        "physics": 30,
        "python": 40
    },
    "prince": {
        "bio": 50,
        "hindi": 40,
        "chemistry": 60,
        "java": 33
    },
    "harshika": {
        "maths": 75,
        "hindi": 67,
        "physics": 40,
        "cpp": 68
    }
}


for name, marks in class_marks.items():
    print("")
    print(name)
    for sub, mark in marks.items():
        print(f"\t{sub}: {mark}")
