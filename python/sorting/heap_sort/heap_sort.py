from max_heapify import max_heapify, swap
from build_max_heap import build_max_heap

def heap_sort(array):
	array = build_max_heap(array)
	sorted_array = []
	# Loop till array has 1 element
	for i in range(len(array)-1,0,-1):
		array = swap(i,0,array)
		maxnum = array[len(array) - 1]
		array.pop(len(array)-1)
		sorted_array.insert(0,maxnum)
		max_heapify(array,0)
	# Insert last element of heap
	sorted_array.insert(0,array[0])
	return sorted_array


array = [34,32,53,42,4,77,3,12,9,31,232,1,2]

print(heap_sort(array))