#Create list
fruits = ["apple", "pear", "kiwi", "banana", "strawberry", "blueberry"]

#Indexing and access operator
print(fruits)
print(fruits[0])
print(fruits[-1])
print(fruits[3])
print(fruits[::-1])

#Loop
for fruit in fruits:
    print(fruit)

#Create new lists
greens = ["tomat", "gurka", "majs", "sallad"]
fruktsallad= []
#Append
for green in greens:
    fruktsallad.append(green)

for fruit in fruits:
    fruktsallad.append(fruit)

print(fruktsallad)

#List comprehension

y = [2*x-2 for x in range(10)]
print(y)
x = [x for x in range(10)]
print(x)

#Plot
import matplotlib.pyplot as plt
plt.plot(x,y)
plt.xlabel="x"
plt.ylabel="y"
plt.title("Graf")
plt.show()

#2D lista
tabell = []

for i in range(11):
    rad = [x*i for x in range(11)]
    tabell.append(rad)
    for j in range(11):
        print(f"{tabell[i][j]:3}", end=" ")

print(tabell)
print(tabell[3])
print(tabell[3][2])