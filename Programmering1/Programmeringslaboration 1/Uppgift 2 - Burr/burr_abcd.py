#A
for i in range(1,101):
    print(i)
    
#B
for i in range(1,101):
    if i % 5 == 0:
        print("Burr")
    else:
        print(i)

#C och D
print("Mata in ett tal vars multiplar blir ”Burr”")
burr = int(input("Input: "))
print("Mata in ett tal vars multiplar blir ”Birr”")
birr = int(input("Input: "))
for i in range(1,101):
    if i % burr == 0:
        print("Burr")
    if i % birr == 0:
        print("Birr")
    else:
        print(i)
