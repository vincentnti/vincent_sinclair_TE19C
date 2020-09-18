x = float(input("X Coordinate: "))
y = float(input("Y Coordinate: "))
location = ""

if x > 0 and y > 0:
    print("kvadrat 1")
    location = "Kvadrat 1"
elif x < 0 and y > 0:
    location = "Kvadrat 2"
elif x < 0 and y <0 :
    location = "Kvadrat 3"
elif x > 0 and y < 0:
    location = "Kvadrat 4"
else:
    location = "Origo"

print(f"Punkt ({x},{y}) befinner sig i {location}")