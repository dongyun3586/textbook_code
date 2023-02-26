from random import randint

def partition(array, low, high):
    print(f'partition(arr, {low}, {high})')
    mid = (low + high) // 2
    pivot = array[mid]  # 가운데 요소를 피벗으로 선택
    print(f'pivot={pivot}, mid={mid}, low={low}, high={high}')

    # 모든 요소 순회 각 요소를 피벗값과 비교
    while low <= high:
        while array[low] < pivot: low += 1
        while array[high] > pivot: high -= 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
            low, high = low + 1, high - 1
        print(f'{arr}, low={low}, high={high}')
    print(f'partition 분할 완료: {arr}, low={low}, high={high}')
    return low  # 파티션이 완료된 위치 반환


def quickSort(array, start, end):
    print(f'quickSort(arr, {start}, {end})')
    if start >= end:
        return
    p = partition(array, start, end)
    quickSort(array, start, p - 1)
    quickSort(array, p, end)


# for _ in range(50):
#   arr = [randint(0, 10) for _ in range(8)]
#   print('정렬 전  :', arr)
#   quickSort(arr, 0, len(arr) - 1)
#   print('정렬 후  :', arr, arr == sorted(arr))

arr = [6, 3, 10, 5, 3, 1, 2]
# arr = [1, 2, 3, 4, 6, 7, 10]
arr = [5, 4, 3, 2, 1]
print('정렬 전  :', arr)
quickSort(arr, 0, len(arr) - 1)
print('정렬 후  :', arr)