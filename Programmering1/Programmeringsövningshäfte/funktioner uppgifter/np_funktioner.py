import math
import matplotlib.pyplot as plt

def calc_pop(t):
    return 11/(1+3.4*math.exp(-0.03*t))

print(calc_pop(0))
#2,5 miljarder

print(calc_pop(99999999))
#11 miljarder

tests = []
for i in range(1000):
    tests.append(calc_pop(i))
plt.plot(tests)
plt.ylabel("Population")
plt.xlabel("Years after 1950")
plt.show()