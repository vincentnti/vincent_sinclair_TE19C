#a
def summa(n):
    return 2 * n + 1

n = int(input("Set n: "))
print(f"Svaret blir {summa(n)} på position {n}")
#b

ns = int(input("Set n start: "))
nf = int(input("Set n final: "))

def iter_summa(ns, nf):
    for i in range(ns, nf + 1):
        print(summa(i))
#INTE KLAR