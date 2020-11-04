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
print("Input a whole number")
answer = int(input("Input: "))

if answer % 5 == 0:
    print("Burr")
elif answer % 3 == 0:
    print("Birr")
else:
    print(answer)
