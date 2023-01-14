from random import randint

def quick_sort(arr, start, end):
    if start >= end:
        return
    pivot = start   # arr의 첫 번째 index를 pivot으로 지정
    low, high = start + 1, end

    while low <= high:
        while low <= end and arr[low] <= arr[pivot]: low += 1
        while high > start and arr[high] >= arr[pivot]: high -= 1
        if low > high:
            arr[high], arr[pivot] = arr[pivot], arr[high]
        else:
            arr[high], arr[low] = arr[low], arr[high]
    quick_sort(arr, start, high - 1)
    quick_sort(arr, high + 1, end)


for _ in range(50):
  arr = [randint(10, 90) for _ in range(8)]
  print('정렬 전  :', arr)
  quick_sort(arr, 0, len(arr) - 1)
  print('정렬 후  :', arr, arr == sorted(arr))

# arr = [69, 10, 30, 2, 16, 8, 31, 22]
# print('정렬 전  :', arr)
# quick_sort(arr, 0, len(arr) - 1)
# print('정렬 후  :', arr)