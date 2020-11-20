import matplotlib.pyplot as plt

kvadrater = [x**2 for x in range(-10,11)]
print(kvadrater)

plt.plot(kvadrater)
plt.show()