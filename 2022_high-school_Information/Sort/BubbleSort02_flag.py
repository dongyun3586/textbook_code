def bubble_sort(nums):
    for i in range(1, len(nums)):
        swapped = False
        for j in range(len(nums) - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True
        if not swapped:
            break


nums = [6, 10, 4, 2, 3, 1, 7]
nums = list(range(5, 0, -1))
bubble_sort(nums)
print(nums)
