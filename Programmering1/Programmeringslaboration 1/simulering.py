import math
import random

#Point coordinates
#point = {"x_coordinate" : 0.0, "y_coordinate" : 0.0}





class Board:
    points = []
    radius = 1
    circle_area = math.pi * radius**2

    def __init__ (self):
        for _ in range(0,100):
            self.points.append(Point())

    def check_board (self):
        for point in self.points:
            print(point.x, point.y)
            self.in_circle(self.calc_distance(point.x, point.y))

    def calc_distance (self, x, y):
        math.sqrt(x**2 + y**2)
    
    def in_circle (self, distance):
        if distance <= self.radius:
            return True
        else:
            return False
        
class Point:
    x: float
    y: float

    def __init__ (self):
        self.x = random.uniform(-1,1)
        self.y = random.uniform(-1,1)

b = Board()
b.check_board()
#print(point["x_coordinate"])

#Points history container
points = []



random.seed()

#def throw_dart (x_coordinate, y_coordinate):
    #print("Wee")


def random_coordinates (x_coordinate, y_coordinate):
    return
    

#def calc_distance (x_coordinate, y_coordinate):
    #return math.sqrt(x_coordinate**2 + y_coordinate**2)

#To know wheter a point is within the circle we can check wheter the distance from the origon to the point is less than the radius of the circle
def in_circle (distance):
    if distance <= radius:
        return True
    else:
        return False

distance = calc_distance(-0.5, -0.5)
print("Distance: " + str(distance))
ans = in_circle(distance)
print(ans)

#for i in range(0,1000):
    #print(random.uniform(-1,1))

