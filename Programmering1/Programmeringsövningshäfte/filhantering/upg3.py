import matplotlib.pyplot as plt

files = ['NPvt19Ma2A.txt', 'NPvt19Ma2C.txt']

for file in files:
    with open(file, 'r') as file:
        labels = []
        sizes = []
        for line in file:
            line = line.replace('%', '')

            percent = float(line[2:])
            if percent != 0.0:
                sizes.append(percent)
                labels.append(line[0])

        fig, ax1 = plt.subplots()
        ax1.pie(sizes, labels=labels, autopct='%1.1f%%') #Autopct allows us to draw the percentage on the slices
        ax1.axis('equal') #Used for keeping circle form by setting axis to an equal aspect ratio.

        plt.show()

        print('LABEL:', labels, 'SIZES:', sizes) #Debug
