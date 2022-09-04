def binarySearch(dataList, key):
    low = 0
    high = len(dataList) - 1
    while low <= high:
        mid = (low + high) // 2
        if key < dataList[mid]:
            high = mid - 1
        elif key == dataList[mid]:
            return mid
        else:
            low = mid + 1
    return -1


def main():
    lst = [20, 50, 12, 7, 30, 8, 11, 33, 56, 19]
    while True:
        x = eval(input("What number do you want (999 to exit): "))
        lst.sort()
        ans = binarySearch(lst, x)
        if x != 999:
            if ans != -1:
                print(f"{x} is at list[{ans}]")
            else:
                print(f"{x} is not found")
        else:
            print('Finish')
            break


main()
