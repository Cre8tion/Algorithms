from max_heapify import max_heapify

# Array must be Max_Heap
def extract_max(array):
	max = array[0]
	array[0] = array[len(array)-1]
	array.pop(len(array)-1)
	max_heapify(array,0)
	print(array)
	return max


array = [8,5,7,4,3,5,3,1,2]

extract_max(array)