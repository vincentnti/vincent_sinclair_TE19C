import matplotlib.pyplot as plt
import numpy

a_vals = []

for x in range(1,10000):
    a = round(5*(2+4/x),2)
    a_vals.append(a)

print(a_vals)

plt.plot(a_vals)
plt.show()

#Gå till kod stugan