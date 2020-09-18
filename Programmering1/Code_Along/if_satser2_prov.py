#Exempel program för att sätta betyg på elever.
import random

betyg = ""
klass = ["Kokchun", "Tommy", "Henrick", "Zsofia", "Simon", "Tatiana"]

for x in klass:
    points = random.randint(0,65)
    if points > 60:
        betyg = "A"
    elif points > 56:
        betyg = "B"
    elif points > 51:
        betyg = "C"
    elif points > 41:
        betyg = "D"
    elif points > 30:
        betyg = "E"
    else:
        betyg = "F"
    print(x, points, betyg)

""" #Less clean version
if points > 60:
    print("A")
elif points >= 56 and points <= 60:
    print("B")
elif points >= 51 and points <= 55:
    print("C")
elif points >= 41 and points <= 50:
    print("D")
elif points >= 31 and points <= 40:
    print("E")
elif points < 30:
    print("F")
else:
    print("A")
"""