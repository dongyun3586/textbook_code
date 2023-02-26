from random import randint

def partition(arr, start, end):
    pivot = arr[start]                   # arr의 첫 번째 요소의 index를 pivot으로 지정
    low, high = start + 1, end      # low, high 지정

    # 모든 요소 순회 각 요소를 pivot과 비교
    while low <= high:
        while low <= high and arr[low] <= pivot: low += 1       # pivot 보다 큰 값 찾기

        while low <= high and arr[high] > pivot: high -= 1    # pivot 보다 작은 값 찾기

        # 만약 low와 high가 교차하지 않았으면 low와 high의 값을 서로 교환
        if low < high:
            arr[high], arr[low] = arr[low], arr[high]
            low, high = low + 1, high - 1

    # low와 high가 교차했으면 pivot과 high의 값을 교환
    arr[high], arr[start] = arr[start], arr[high]

    return high             # 파티션이 완료된 위치 반환


def quickSort(arr, start, end):
    if start >= end:
        return
    p = partition(arr, start, end)
    quickSort(arr, start, p - 1)
    quickSort(arr, p + 1, end)


for _ in range(50):
  arr = [randint(10, 90) for _ in range(8)]
  print('정렬 전  :', arr)
  quickSort(arr, 0, len(arr) - 1)
  print('정렬 후  :', arr, arr == sorted(arr))

# arr = [3,8,3,10,2,9,3,1]
# print('정렬 전  :', arr)
# quickSort(arr, 0, len(arr) - 1)
# print('정렬 후  :', arr)