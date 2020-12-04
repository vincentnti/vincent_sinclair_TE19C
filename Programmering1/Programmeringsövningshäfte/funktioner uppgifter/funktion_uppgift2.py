#a
def summa(n):
    answer = 0
    for i in range(n):
        answer += 2*i+1
    return answer

n = int(input("Set n: "))
print(f"Svaret blir {summa(n)}")
#b

ns = int(input("Set n start: "))
nf = int(input("Set n final: "))

def iter_summa(ns, nf):
    answer = 0
    for i in range(ns + 1,nf):
        answer += 2*i+1
    return answer

print(f"Svaret blir {iter_summa(ns, nf)}")

#allt ska göras om gjorde fel i början visste inte att
#man skulle lägga ihop det