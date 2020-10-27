import math

radius = 1
circle_area = math.pi * (radius**2)
square_area = (radius + radius) * (radius + radius)

print("Radius: ", radius)
print("Circle Area: ", circle_area)
print("Square Area: ", square_area)

print("Ratio: ", circle_area/square_area)
print("Ratio * 4: ", (circle_area/square_area) * 4)