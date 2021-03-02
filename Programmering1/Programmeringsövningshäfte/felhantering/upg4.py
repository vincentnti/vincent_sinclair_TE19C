#Not done
def calc_median():
    print("cheese")


try:
    print("Skriv in 5 tal med mellanrum mellan varje tal")
    numbers = input("Tal:")
    numbers = numbers.split()
    assert(len(numbers) == 5)
    for i, number in enumerate(numbers):
        numbers[i] = int(number)

except AssertionError:
    print(AssertionError)
except ValueError:
    print(ValueError)
except:
    pass