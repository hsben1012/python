array = [[11, 12, 13], [21, 22, 23], [31, 32, 33], [1, 2, 3]]
temp = 0
rowIndex = 0

for row in array:
    if temp < sum(row):
        temp = sum(row)
        rowIndex = array.index(row)
print(temp)
print(rowIndex)
