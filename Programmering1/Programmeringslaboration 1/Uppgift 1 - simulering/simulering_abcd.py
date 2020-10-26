import math
import random
#A
print("A_distance:", math.sqrt(0.5**2 + 0.5**2))

#B
print("B_distance:", math.sqrt(1**2 + 1**2))

#C
#Då distansen från origo alltid kommer vara över noll och **2 inte konverterar ett negativt tall till positivt i python av någon anledning
#kan vi använda oss av abs() för att alltid ha positiva värden
print("Some examples of this not working ", "Ex1: ", -1**2, "Ex2: ", (1**2) + (-1**2))

print("C_distance: ", math.sqrt(abs(0.5**2) + abs(-0.5**2)))

#D
class Point:
    x: int
    y: int
    def __init__ (self):
        self.x = random.uniform(-1,1)
        self.y = random.uniform(-1,1)

for i in range(0,3):
    point = Point()
    print("X: ", point.x, "Y: ", point.y)