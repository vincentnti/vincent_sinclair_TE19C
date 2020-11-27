#a
def summa(n, a, an):
    return (n * (a + n)/2)

print(summa(1,2,2))

#b
print(summa(100, 1, 100))

#c
n = int(input("Set n: "))
a = int(input("Set a: "))
an = int(input("Set an: "))
print("The Answer:", summa(n,a,an))