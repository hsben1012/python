def getData():
    array = []
    numberRows = eval(input('How many rows? '))
    numberColumns = eval(input('How many columns? '))
    for row in range(numberRows):
        array.append([])
        for column in range(numberColumns):
            data = eval(input('Enter a value and press Enter: '))
            array[row].append(data)
    return array


def total(array):
    ttl = 0
    for row in array:
        ttl += sum(row)
    return ttl


def main():
    arrayData = getData()
    print(arrayData)
    print(f"Sum of all elements is {total(arrayData)}")


main()
