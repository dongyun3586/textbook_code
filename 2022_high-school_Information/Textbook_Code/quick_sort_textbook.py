from random import randint

def partition(arr, start, end):
    print(f'partition(arr, {start}, {end})')
    pivot = arr[start]                      # arr의 첫 번째 요소의 index를 pivot으로 지정
    low, high = start + 1, end              # low, high 지정
    print(f'pivot={pivot}, low={low}, high={high}')

    # 모든 요소 순회 각 요소를 pivot과 비교
    while low <= high:
        while low <= high and arr[low] <= pivot: low += 1       # pivot 보다 큰 값 찾기
        while low <= high and arr[high] > pivot: high -= 1    # pivot 보다 작은 값 찾기

        # 만약 low와 high가 교차하지 않았으면 low와 high의 값을 서로 교환
        if low < high:
            arr[high], arr[low] = arr[low], arr[high]
        print(f'{arr}, low={low}, high={high}')

    # low와 high가 교차했으면 pivot과 high의 값을 교환
    arr[high], arr[start] = arr[start], arr[high]

    print(f'partition 분할 완료: {arr}, low={low}, high={high}')

    return high             # 파티션이 완료된 위치 반환


def quickSort(arr, start, end):
    print(f'quickSort(arr, {start}, {end})')
    if start >= end:
        return
    p = partition(arr, start, end)
    quickSort(arr, start, p - 1)
    quickSort(arr, p + 1, end)


arr = [4, 6, 10, 2, 3, 1, 7]
# arr = [1, 2, 3, 4, 6, 7, 10]
arr = [10, 7, 6, 4, 3, 2, 1]
arr = [7, 6, 5, 4, 3, 2, 1]
# arr = [4, 5, 7, 6, 2, 1, 3]
# arr = [3, 5, 4, 1, 2]
print('정렬 전  :', arr)
quickSort(arr, 0, len(arr) - 1)
print('정렬 후  :', arr)