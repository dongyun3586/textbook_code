def binary_search(array, value, low, high):
	if low > high:
		return False
	mid = (low+high) // 2
	if array[mid] > value:
		return binary_search(array, value, low, mid-1)
	elif array[mid] < value:
		return binary_search(array, value, mid+1, high)
	else:
		return mid

arr = [1, 2, 3, 4, 5, 6, 7, 10]
value = 10
low = 0
high = len(arr) - 1

print(binary_search(arr, value, low, high))