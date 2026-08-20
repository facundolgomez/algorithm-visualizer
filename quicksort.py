def quicksort(arr):
	if len(arr) in (0,1):
		return arr
	pivot = arr[0]
	less_than_pivot = [x for x in arr[1:] if x <= pivot]
	greater_than_pivot = [x for x in arr[1:] if x > pivot]
	left_array = quicksort(less_than_pivot)
	right_array = quicksort(greater_than_pivot)
	return left_array + [pivot] + right_array