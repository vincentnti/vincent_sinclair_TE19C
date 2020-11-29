rows = []
chessletters = ["a", "b", "c", "d", "e", "f", "g", "h"]
for i in range(1,9):
    rows.append([str(i) + letter for letter in chessletters])

print(rows)