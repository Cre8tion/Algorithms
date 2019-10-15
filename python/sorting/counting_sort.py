'''
This implementation of counting sort takes k to be the maximum value in the array.
O(n+k) can be O(k) if k is large

We assume all the values are >= 0
'''

def counting_sort_basic(array):
	max_value = 0
	for i in range(len(array)):
		max_value = max(max_value,array[i])

	count_array = [0] * (max_value + 1)

	for i in range(len(array)):
		count_array[array[i]] += 1

	sorted_array = [0] * len(array)
	idx = 0

	for i in range(len(count_array)):
		if(count_array[i] != 0):
			count = count_array[i]
			while(count > 0):
				sorted_array[idx] = i
				idx += 1
				count -= 1

	return sorted_array

'''
This alternative implementation of counting sort takes k to be the maximum value in the array.
O(n+k) can be O(k) if k is large

We assume all the values are >= 0

Can be used for non-numeric items;
Does not create a new array to accumulate count for sorting;
'''

def counting_sort_basic_alt(array):
	max_value = 0
	for i in range(len(array)):
		max_value = max(max_value,array[i])

	count_array = [0] * (max_value + 1)

	for i in range(len(array)):
		count_array[array[i]] += 1

	# Adding in-place
	for i in range(len(count_array)):
		if(i > 0): 
			count_array[i] = count_array[i] + count_array[i - 1]

	#Shift Right
	count_array.pop()
	count_array.insert(0,0)

	sorted_array = [0] * len(array)

	for i in range(len(array)):
		value = array[i]
		sorted_array[count_array[value]] = value
		count_array[value] += 1

	return sorted_array



array = [5,2,9,5,2,3,5,4]

print(counting_sort_basic(array))
print(counting_sort_basic_alt(array))