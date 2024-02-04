def quick_sort(nums, start, end):
    if start >= end:
        return
    pivot = start  # arr의 첫 번째 요소를 pivot으로 지정
    low, high = start + 1, end  # low, high 지정

    # 모든 요소 순회: 각 요소를 pivot과 비교
    while low <= high:
        while low <= high and nums[low] <= nums[pivot]: low += 1  # pivot 보다 큰 값 찾기
        while low <= high and nums[high] >= nums[pivot]: high -= 1  # pivot 보다 작은 값 찾기

        # 만약 low와 high가 교차하지 않았으면 low와 high의 값을 서로 교환
        if low < high:
            nums[high], nums[low] = nums[low], nums[high]

    # pivot과 high 교환
    nums[high], nums[pivot] = nums[pivot], nums[high]
    print(f'partition 분할 완료: {nums}, low={low}, high={high}')

    quick_sort(nums, start, high - 1)
    quick_sort(nums, high + 1, end)


nums = [4, 6, 10, 2, 3, 1, 7]
nums = [7, 9, 6, 2, 1, 3]
# # arr = [1, 2, 3, 4, 6, 7, 10]
# arr = [10, 7, 6, 4, 3, 2, 1]
# arr = [7, 6, 5, 4, 3, 2, 1]
# # arr = [4, 5, 7, 6, 2, 1, 3]
# # arr = [3, 5, 4, 1, 2]
# arr = [6, 10, 4, 2, 3, 1, 7]
print('정렬 전  :', nums)
quick_sort(nums, 0, len(nums) - 1)
print('정렬 후  :', nums)
