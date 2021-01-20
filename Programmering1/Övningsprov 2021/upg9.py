def generate_pattern(n):
    rows = [[0, 1, 0]]
    for i in range(n):
       #Calculate problem amount
        problem_amount = len(rows[i]) - 1
        print(problem_amount)
        rows.append([])
        #Add everything next to each other together
        for z in range(problem_amount):
            rows[i + 1].append(rows[i][z] + rows[i][z+1])
        #Add unseen zeros
        rows[i + 1].insert(0,0)
        rows[i + 1].append(0)

    return rows

def draw_pattern(rows):
    for i, row in enumerate(rows):
        print(" " * (len(rows) - i), end="") #Offset
        for z in range(len(row)):
            #Print everything on the row aside from the invisible zeros
            if row[z] != 0:                
                print(row[z], end=" ")
        print("\n")

n = int(input("Set N: ")) #N def = 6
rows = generate_pattern(n)
draw_pattern(rows)