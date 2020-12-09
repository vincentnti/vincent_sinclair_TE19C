#a
def fakultet(n):
    for i in range(n-1, 1, -1):
        n *= i
    return n

print(fakultet(2))
print(fakultet(5))

#b
def divd(n):
    answer = 1
    for i in range(1,n + 1):
        answer += 1/fakultet(i)
    return answer

print(divd(100))

#c
def div_udda (n):
    answer = 0.0
    for i in range(1, n + 1):
        answer += ((-1)**(i+1))/(2*i-1)
    return answer

print("Summa: ", div_udda(3))
