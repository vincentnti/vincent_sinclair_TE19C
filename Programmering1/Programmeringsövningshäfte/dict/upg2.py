import random

results = {
    1 : 0,
    2 : 0,
    3 : 0,
    4 : 0,
    5 : 0,
    6 : 0
}

antal_kast = 100000
for i in range(antal_kast):
    results[random.randint(1,6)] += 1

for key, item in results.items():
    print(f"{key}: {item}")