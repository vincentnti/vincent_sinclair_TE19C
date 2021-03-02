import random
tests = [10, 100, 1000, 10000, 100000]

dice_throw_data = {
    'total': 0,
    '1': 0,
    '2': 0,
    '3': 0,
    '4': 0,
    '5': 0,
    '6': 0
}

def roll_dice():
    return random.randint(1,6)

def write_to_file():
    file.write("Total: " + str(dice_throw_data['total']) + "\n")

    #Skip first item aka 'total' (Could also seperate total but doesn't really matter)
    iter_dice_throw_data = iter(dice_throw_data)
    next(iter_dice_throw_data)

    for item in iter_dice_throw_data:
        calc_probability = str(dice_throw_data[item] / dice_throw_data['total'])
        file.write(item + ': ' + 'Kast: ' + str(dice_throw_data[item]) + ' Sannolikhet: ' + calc_probability + '\n')

with open('simulering.txt', 'w') as file:
    for test in tests:
        dice_throw_data.clear
        for simulations in range(test):
            dice_throw_data[str(roll_dice())] += 1
            dice_throw_data['total'] = simulations + 1
        
        write_to_file()


