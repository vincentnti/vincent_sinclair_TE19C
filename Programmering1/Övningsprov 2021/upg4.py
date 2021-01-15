import math
def calc_sphere_volume(radius):
    return 4/3*math.pi*radius**3

radius = int(input("Sätt radien: "))
print("Volymen på sfären är",calc_sphere_volume(radius))