import random
kast = []

for i in range(10):
    kast.append(random.randint(1,6))

print(kast)

#a
kast.sort()
print(kast)

#b
kast.sort(reverse=True)
print(kast)
