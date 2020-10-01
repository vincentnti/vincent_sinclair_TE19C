results = [1]
denominator = 1
for i in range(1,111):
    denominator *= 2
    results.append(1/denominator)

    print("Denominator: ",denominator)

print("Konvergerar mot: ", sum(results))

