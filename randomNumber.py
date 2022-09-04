import random
evenCount = 0
oddCount = 0

for i in range(1, 101):
    randomNumber = random.randint(1, 100)
    if i % 10 == 0:
        print('{0:<3d}'.format(randomNumber))
    else:
        print('{0:<3d}'.format(randomNumber), end=' ')
    if randomNumber % 2 == 0:
        evenCount += 1
    else:
        oddCount += 1
print('\neven number: ', evenCount, '\nodd number: ', oddCount)
