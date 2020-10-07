results = [1]
i = 0
denominator = 1

while i < 111:
    denominator *= 2
    results.append(1/denominator)
    i+=1

print(results)
print(f"Det konvergerar mot talet {sum(results)}")