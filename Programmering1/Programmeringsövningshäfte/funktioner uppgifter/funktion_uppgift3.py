import math
#a
print(math.sqrt((5**2 + 2**2)))

#b
class Point:
    x: int
    y: int
    
    def __init__  (self):
        self.x = int(input("Set x coordinate for point: "))
        self.y = int(input("Set y coordinate for point: "))

def calc_dist_points(point_a, point_b):
    xdist = abs(point_a.x - point_b.x) 
    ydist = abs(point_a.y - point_b.y)

    return math.sqrt(xdist**2 + ydist**2)

#c
print("Distance:", calc_dist_points(point_a = Point(), point_b = Point()))
