radie = float(input("Radie: "))

if radie > 0: 
    area = radie**2 * 3.14 
    print("Area: ", area)
    omkrets = radie * 2 * 3.14
    print("Omkrets:", omkrets)
else:
    print("Error: Positive value required!")

