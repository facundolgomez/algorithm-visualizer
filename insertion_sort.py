def insertion_sort(arr):
	for i in range(0, len(arr) - 1):
		key = arr[i + 1]
		j = i
		while j >= 0 and arr[j] > key:
			arr[j + 1] = arr[j]
			j = j - 1

		arr[j + 1] = key

	return arr


