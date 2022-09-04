number1 = eval(input('Please enter an integer1:\n'))
number2 = eval(input('Please enter an integer2:\n'))
gcd = 1
k = 2
while k <= number1 and k <= number2:
    if number1 % k == 0 and number2 % k == 0:
        gcd = k
    k += 1
print('\nThe GCD for', number1, 'and', number2, 'is', gcd)
