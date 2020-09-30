#A
"""
for i in range(1,11):
    print(i * 10)
"""
#B
"""
start = int(input("Start Value: "))
end = int(input("End Value"))
end = end + 1

for i in range(start, end):
    print(i * 10)
"""
#C
"""
counter = 1
x = 0
for i in range(1,111):
    print(counter * x)
    counter += 1
    if counter > 10:
        counter = 1
        x += 1
"""
#C version 2
count=0
for i in range(1,11):
    count+=1
    print("\n ",count, "tabell")
    for j in range(1,11):
        print(count * j, end=" ")

