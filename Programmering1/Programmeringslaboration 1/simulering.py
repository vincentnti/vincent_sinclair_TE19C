import math
import random
x_coordinate = 0.0
y_coordinate = 0.0
radius = 1
circle_area = math.pi * radius**2
print(circle_area)
def throw_dart (x_coordinate, y_coordinate):
    print("Wee")

def calc_distance (x_coordinate, y_coordinate):
    return math.sqrt(x_coordinate**2 + y_coordinate**2)

def random_coordinates ():
    print("t")

def in_circle (distance):
    if distance <= radius:
        return True
    else:
        return False

distance = calc_distance(1, 1)
print("Distance: " + str(distance))
ans = in_circle(distance)
print(ans)

#for i in range(0,1000):
    #print(random.uniform(-1,1))

