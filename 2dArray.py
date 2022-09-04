import random
array = []

numberOfRow = eval(input("Enter the number of rows: "))
numberOfColumn = eval(input("Enter the number of columns: "))
for row in range(numberOfRow):
    array.append([])
    for column in range(numberOfColumn):
        value = random.randint(1, 100)
        array[row].append(value)

for rows in array:
    for columns in rows:
        print(f"{columns:3d}", end=' ')
    print()
