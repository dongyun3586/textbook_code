def binary_search(nums, find_num):
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == find_num:
            return mid
        elif nums[mid] > find_num:
            high = mid - 1
        else:
            low = mid + 1
    return -1

arr = [1, 2, 3, 4, 5, 6, 7, 10]
arr = [1, 2, 3, 4, 5, 6, 10]
value = 10
low = 0
high = len(arr) - 1

result = binary_search(arr, value)
print(result)