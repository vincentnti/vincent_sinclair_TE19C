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
def div_udda (n):
    answer = 0.0
    for i in range(1, n + 1):
        answer += ((-1)**(i+1))/(2*i-1)
        print("Is now:", answer)
    return answer

print("Summa: ", div_udda(3))
