def bubbleSort(x):
    length = len(x) - 1
    for i in range(length):
        for j in range(length - i):
            if x[j] > x[j + 1]:
                x[j], x[j + 1] = x[j + 1], x[j]
    return x


arr = [69, 10, 30, 2, 16, 8, 31, 22]
print('정렬 전: ', arr)
bubbleSort(arr)
print('정렬 후: ', arr)
