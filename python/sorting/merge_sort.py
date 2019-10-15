import math


# Implementation 1

def merge_sort(array):
	if len(array) == 1:
		return array
	elif len(array) == 2:
		if array[0] < array[1]:
			return array
		else:
			return [array[1],array[0]]
	else:
		arr1 = merge_sort(array[:math.floor(len(array)/2)])
		arr2 = merge_sort(array[math.floor(len(array)/2):])
		return merge(arr1,arr2)

def merge(array1,array2):
	lowHalf = array1[:]
	highHalf = array2[:]

	merged_array = []

	i = 0
	j = 0

	while(i < len(lowHalf) and j < len(highHalf)):
		if(lowHalf[i]< highHalf[j]):
			merged_array.append(lowHalf[i])
			i+=1
		else:
			merged_array.append(highHalf[j])
			j+=1

	while(i < len(lowHalf)):
		merged_array.append(lowHalf[i])
		i+=1

	while(j < len(highHalf)):
		merged_array.append(highHalf[j])
		j+=1

	return merged_array


# Implementation 2

def mergeSort(arr): 
    if len(arr) >1: 
        mid = len(arr)//2 #Finding the mid of the array 
        L = arr[:mid] # Dividing the array elements  
        R = arr[mid:] # into 2 halves 
  
        mergeSort(L) # Sorting the first half 
        mergeSort(R) # Sorting the second half 
  
        i = j = k = 0
          
        # Copy data to temp arrays L[] and R[] 
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                arr[k] = L[i] 
                i+=1
            else: 
                arr[k] = R[j] 
                j+=1
            k+=1
          
        # Checking if any element was left 
        while i < len(L): 
            arr[k] = L[i] 
            i+=1
            k+=1
          
        while j < len(R): 
            arr[k] = R[j] 
            j+=1
            k+=1

        return arr

array = [34,32,53,42,4,77,3,12,9,31,232,1,2]

print(merge_sort(array))
print(mergeSort(array))