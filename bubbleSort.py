numbers = [6, 7, 12, 17, 50, 20]
print('Original data:')
for x in numbers:
    print("{0}".format(x), end=' ')

# Bubble sort
for i in range(len(numbers)-1):
    flag = 0  # 如果只需比一次就可以知道結果就break，例如: [6 7 12 17 50 20]
    for j in range(len(numbers)-i-1):
        if numbers[j] > numbers[j+1]:
            flag = 1
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    if flag == 0:
        break

print('\nAfter processing:')
for y in numbers:
    print("{0}".format(y), end=' ')
