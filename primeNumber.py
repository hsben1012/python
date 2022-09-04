number = eval(input('Please enter a number:\n'))
divisor = 2
flag = 1
while divisor < number:
    if number % divisor == 0:
        flag = 0
        break
    divisor += 1
if flag == 0:
    print(number, 'is not prime number.')
else:
    print(number, 'is prime number.')
