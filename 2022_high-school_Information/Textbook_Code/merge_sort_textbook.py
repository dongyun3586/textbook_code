def merge(arr, left, mid, right):
    print(f'merge(arr, {left}, {mid}, {right})')
    i = left        # 왼쪽 리스트에 대한 인덱스
    j = mid + 1     # 오른쪽 리스트에 대한 인덱스
    k = left        # 두 리스트를 정렬하여 저장할 임시 리스트에 대한 인덱스

    # 두 개의 list 병합
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            sorted_list[k] = arr[i]
            k, i = k+1, i+1
        else:
            sorted_list[k] = arr[j]
            k, j = k + 1, j + 1

    # 왼쪽 리스트와 오른쪽 리스트 중 남아있는 값 복사
    if i <= mid:        # 왼쪽 리스트에 남아 있는 값 복사
        for l in range(i, mid+1):
            sorted_list[k] = arr[l]
            k += 1
    else:               # 오른쪽 리스트에 남아 있는 값 복사
        for l in range(j, right+1):
            sorted_list[k] = arr[l]
            k += 1

    # sorted_list의 값을 arr로 복사
    for l in range(left, right+1):
        arr[l] = sorted_list[l]
    # print(arr)


def merge_sort(arr, left, right):

    if left < right:
        print(f'merge_sort(arr, {left}, {right})')
        mid = (left + right) // 2           # 중간 위치를 계산하여 리스트를 균등 분할 -분할(Divide)
        # print(f'mid={mid}, left={left}, right={right}')
        merge_sort(arr, left, mid)          # 중간 위치를 계산하여 리스트를 균등 분할 -분할(Divide)
        merge_sort(arr, mid+1, right)       # 중간 위치를 계산하여 리스트를 균등 분할 -분할(Divide)
        merge(arr, left, mid, right)        # 정렬된 2개의 부분 배열을 합병하는 과정 -결합(Combine)


arr = [69, 10, 30, 2, 16, 8, 31, 22]
arr = [7, 6, 5, 4, 3, 2, 1]
arr = [4, 5, 7, 6, 2, 1, 3]
arr = [4, 6, 10, 2, 3, 1, 7, 5]
sorted_list = [0 for i in range(0, len(arr))]
print('정렬 전  :', arr)
merge_sort(arr, 0, len(arr) - 1)
print('정렬 후  :', arr)


# from random import randint
# for _ in range(50):
#   arr = [randint(0, 10) for _ in range(8)]
#   sorted_list = [0 for i in range(0, len(arr))]
#   print('정렬 전  :', arr)
#   merge_sort(arr, 0, len(arr)-1)
#   print('정렬 후  :', arr, arr == sorted(arr))