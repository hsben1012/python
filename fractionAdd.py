nume1 = eval(input('Please enter an numerator1:\n'))
denom1 = eval(input('Please enter an denominator1:\n'))
nume2 = eval(input('Please enter an numerator2:\n'))
denom2 = eval(input('Please enter an denominator2:\n'))
num1 = nume1 * denom2 + nume2 * denom1
num2 = denom1 * denom2

gcd = 1
k = 2
while k <= num1 and k <= num2:
    if num1 % k == 0 and num2 % k == 0:
        gcd = k
    k += 1
ans1 = num1 / gcd
ans2 = num2 / gcd
print('{0:1d}/{1:1d} + {2:1d}/{3:1d} = {4:.0f}/{5:.0f}'.format(nume1, denom1, nume2, denom2, ans1, ans2))
