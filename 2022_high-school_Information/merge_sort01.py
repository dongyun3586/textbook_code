def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid
    i = j = 0  # Initial index of first and second subarray
    k = left  # Initial index of merged subarray

    L = [arr[left + i] for i in range(0, n1)]
    R = [arr[mid + 1 + i] for i in range(0, n2)]

    # Merge the temp arrays back into arr[l..r]
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if there are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2           # 중간 위치를 계산하여 리스트를 균등 분할 -분할(Divide)
        merge_sort(arr, left, mid)          # 중간 위치를 계산하여 리스트를 균등 분할 -분할(Divide)
        merge_sort(arr, mid+1, right)     # 중간 위치를 계산하여 리스트를 균등 분할 -분할(Divide)
        merge(arr, left, mid, right)        # 정렬된 2개의 부분 배열을 합병하는 과정 -결합(Combine)


arr = [69, 10, 30, 2, 16, 8, 31, 22]
print('정렬 전  :', arr)
merge_sort(arr, 0, len(arr) - 1)
print('정렬 후  :', arr)