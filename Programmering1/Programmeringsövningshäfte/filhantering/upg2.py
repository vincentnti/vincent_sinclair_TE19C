#Reset file
with open('Provresultat.bak', "r") as backup:
    with open('Provresultat.txt', 'w') as file:
        for line in backup:
            file.write(line)
            
# Shared
with open('Provresultat.txt', 'r') as f:
    FILE_CONTENTS = f.readlines()

# Solution for 2a
for line in FILE_CONTENTS:
    print(line)

# Solution for 2b
with open('Provresultat.txt', 'a+') as f:
    f.write("\n") #Seperation
    rows = FILE_CONTENTS
    rows.sort()
    f.writelines(rows)

# Solution for 2c
grades = {
    'F': [],
    'E': [],
    'D': [],
    'C': [],
    'B': [],
    'A': []
}

def get_score(row):
    return int(row[-3:])

def get_grade(score):
    conditions = [20, 30, 40, 50, 60, 100]
    for i, grade in enumerate(grades):
        if score < conditions[i]:
            return grade

def sort_students_by_grade(row):
    score = get_score(row)
    grade = get_grade(score)
    grades[grade].append(row)

with open('Provresultat.txt', 'a+') as f:
    f.write("\n") #Seperation
    rows = FILE_CONTENTS

    for row in rows:
        sort_students_by_grade(row)

    for i, grade in enumerate(grades):
        f.write(grade + '\n')
        f.writelines(grades[grade]) 