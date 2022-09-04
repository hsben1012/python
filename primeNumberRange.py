count = 1
for number in range(2, 1001):
    divisor = 2
    flag = 1
    while divisor < number:
        if number % divisor == 0:
            flag = 0
            break
        divisor += 1
    if flag != 0:
        if count % 10 != 0:  # 10 items in row
            print('{0:<3d}'.format(number), end=' ')
        else:
            print('{0:>3d}'.format(number))
        count += 1
