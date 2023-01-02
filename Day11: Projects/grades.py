"""
marks = [89, 59, 65, ......] len() = 10
90-100: A
80-90: B
80-70: C
70-60: D
60-50: E
50: F (else)
"""
marks=[95,64,86,30,74,89,52,50,69,96]
for i in marks:
    if i>90:
        print("A grade")
    elif i<=80 and i<90:
        print("B grade")
    elif i<=70 and i<80:
        print("C grade")
    elif i<=60 and i<70:
        print("D grade")
    elif i>50 or i<60:
        print("E grade")
    elif i>40 or i<=50:
        print("f grade")
    elif i<40:
        print("Fail")
        
"""
marking.py
grades = ['A', 'B', 'C', .......]
marks = input()
print(grade -> marks)
"""


