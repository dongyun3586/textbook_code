def linear_search(nums, find_num):
    for i in range(len(nums)):
        if nums[i] == find_num:
            return i
    return -1


nums = [4, 6, 10, 2, 3, 1, 7]
print(linear_search(nums, 2))
