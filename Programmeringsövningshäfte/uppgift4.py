#Uppgift 4
import math
#A
"""
x1 = 2
y1 = 3

x2 = -2
y2 = 2
"""
# Svar= 4.123105625617661
#B
"""
x1 = 2
y1 = 1

x2 = 1
y2 = 0
"""
# Svar= 1.4142135623730951
#C
x1 = float(input("X1: "))
y1 = float(input("Y1: "))

x2 = float(input("X2: "))
y2 = float(input("Y2: "))

#Alla
answer = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(answer)