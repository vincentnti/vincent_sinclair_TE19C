#a
def fakultet(n):
    for i in range(n-1, 1, -1):
        n *= i
    return n

print(fakultet(2))
print(fakultet(5))

#b
def divd(s):
    for i in range(1,100 + 1):
        s += s/fakultet(i)
    return s

print(divd(1))

#c
#Inte klar med denna
