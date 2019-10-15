from max_heapify import max_heapify

def build_max_heap(array):
	index = (len(array) // 2)
	# starting index should be the last index which nodes are not leaves
	lst = list(range(index))
	lst.reverse()
	for i in lst:
		max_heapify(array,i)
	return array


array = [4,1,3,2,16,9,10,14,8,7]

#print(build_max_heap(array))