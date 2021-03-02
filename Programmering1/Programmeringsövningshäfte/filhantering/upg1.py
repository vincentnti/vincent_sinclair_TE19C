import random

with open("diceRoll.txt", "w") as f:
    rolls = []
    for i in range(10):
        rolls.append(str(random.randint(1,6)))
    #A
    f.write("10 kast: " + " ".join(rolls) + "\n")
    #B
    rolls.sort()
    f.write("Sorterad: " + " ".join(rolls) + "\n")
    #C
    f.write("Antal Femmor: " + str(" ".join(rolls).count("5")))

