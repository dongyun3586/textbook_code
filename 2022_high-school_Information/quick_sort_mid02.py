from random import randint

def partition(array, low, high):
    pivot = array[(low + high) // 2]  # 가운데 요소를 피벗으로 선택

    # 모든 요소 순회 각 요소를 피벗값과 비교
    while low <= high:
        while array[low] < pivot: low += 1
        while array[high] > pivot: high -= 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
            low, high = low + 1, high - 1
    return low  # 파티션이 완료된 위치 반환


def quickSort(array, low, high):
    if low >= high:
        return
    p = partition(array, low, high)
    quickSort(array, low, p - 1)
    quickSort(array, p, high)


for _ in range(50):
  arr = [randint(0, 10) for _ in range(8)]
  print('정렬 전  :', arr)
  quickSort(arr, 0, len(arr) - 1)
  print('정렬 후  :', arr, arr == sorted(arr))