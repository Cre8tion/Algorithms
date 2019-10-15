def insertion_sort(array):
	for idx in range(1,len(array)):
		current_value = array[idx]
		prev_idx = idx - 1
		while prev_idx >= 0 and array[prev_idx] > current_value:
			array[prev_idx + 1] = array[prev_idx]
			prev_idx = prev_idx - 1
		array[prev_idx + 1] = current_value
	return array 

array = [34,32,53,42,4,77,3,12,9,31,232,1,2]

print(insertion_sort(array))
