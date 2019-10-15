def swap(a,b,array):
	temp = array[a]
	array[a] = array[b]
	array[b] = temp
	return array

def bubble_sort(array):
	for i in range(len(array),-1,-1):
		for j in range(i-1):
			if(array[j] > array[j+1]):
				array = swap(j,j+1,array)
	return array


array = [34,32,53,42,4,77,3,12,9,31,232,1,2]

print(bubble_sort(array))