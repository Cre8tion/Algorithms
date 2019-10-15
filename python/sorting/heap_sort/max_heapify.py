# Index in python start with 0 instead of 1

def swap(a,b,array):
	temp = array[a]
	array[a] = array[b]
	array[b] = temp
	return array

def max_heapify(array,idx):
	left = (idx * 2) + 1
	right = (idx * 2) + 2
	if(left < len(array) and array[left] > array[idx]):
		largest = left
	else:
		largest = idx
	if(right < len(array) and array[right] > array[largest]):
		largest = right
	if(largest != idx):
		array = swap(largest,idx,array)
		return max_heapify(array,largest)
	else:
		return array
