from random import randint

def quick_sort(arr, start, end):
    if start >= end:
        return
    pivot = arr[start]                   # arr의 첫 번째 요소의 index를 pivot으로 지정
    low, high = start + 1, end      # low, high 지정

    while low <= high:      # low와 high가 교차할 때까지 반복
        while low <= high and arr[low] <= pivot: low += 1       # pivot 보다 큰 값 찾기
        # while high > start and arr[high] >= pivot: high -= 1   # pivot 보다 작은 값 찾기
        while low <= high and arr[high] >= pivot: high -= 1  # pivot 보다 작은 값 찾기

        # 만약 low와 high가 교차하지 않았으면 low와 high의 값을 서로 교환
        if low < high:
            arr[high], arr[low] = arr[low], arr[high]

    # low와 high가 교차했으면 pivot과 high의 값을 교환
    arr[high], arr[start] = arr[start], arr[high]

    quick_sort(arr, start, high - 1)
    quick_sort(arr, high + 1, end)


for _ in range(50):
  arr = [randint(10, 90) for _ in range(8)]
  print('정렬 전  :', arr)
  quick_sort(arr, 0, len(arr) - 1)
  print('정렬 후  :', arr, arr == sorted(arr))

# arr = [47, 52, 18, 60, 47, 66, 26, 48]
# print('정렬 전  :', arr)
# quick_sort(arr, 0, len(arr) - 1)
# print('정렬 후  :', arr)