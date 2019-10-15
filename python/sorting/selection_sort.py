def selection_sort(array):
	for i in range(len(array)):
		min_value = array[i]
		min_idx = i
		for j in range(i,len(array)):
			if(min_value > array[j]):
				min_idx = j
				min_value = array[j]
		temp = array[i]
		array[i] = array[min_idx]
		array[min_idx] = temp
	return array

array = [34,32,53,42,4,77,3,12,9,31,232,1,2]

print(selection_sort(array))