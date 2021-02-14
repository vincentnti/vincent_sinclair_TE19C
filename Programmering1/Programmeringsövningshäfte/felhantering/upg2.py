def är_fyrsiffrigt(tal):
    calc = abs(tal/1000)
    return calc >= 1 and calc < 10
   
testtal = [999, 1000, 100, 231, 10000, 10001, -1000, 102313]

for tal in testtal:
    if är_fyrsiffrigt(tal):
        print(tal, "är fyrsiffrigt")
    else:
        print(tal, "är inte fyrsiffrigt")