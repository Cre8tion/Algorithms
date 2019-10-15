class Heap:
	def __init__(self, heap=None):
		if heap is None:
			self.heap = []
		else:
			self.heap = heap
			self.build_max_heap()

	def __repr__(self):
		return 'Heap({!r})'.format(self.heap)

	def __str__(self):
		return str(self.heap)

	def swap(self,a,b,array):
		temp = array[a]
		array[a] = array[b]
		array[b] = temp
		return array

	def max_heapify(self,idx):
		heap = self.heap
		left = (idx * 2) + 1
		right = (idx * 2) + 2
		if(left < len(heap) and heap[left] > heap[idx]):
			largest = left
		else:
			largest = idx
		if(right < len(heap) and heap[right] > heap[largest]):
			largest = right
		if(largest != idx):
			heap = self.swap(largest,idx,heap)
			return self.max_heapify(largest)
		else:
			return heap

	def build_max_heap(self):
		heap = self.heap
		index = (len(heap) // 2)
		# starting index should be the last index which nodes are not leaves
		lst = list(range(index))
		lst.reverse()
		for i in lst:
			self.max_heapify(i)
		self.heap = heap

	def extract_max(self):
		max = self.heap[0]
		self.heap[0] = self.heap[len(self.heap)-1]
		self.heap.pop(len(self.heap)-1)
		self.max_heapify(0)
		return max

	def max(self):
		return self.heap[0]

	def increase_key(self,i,k):
		if(self.heap[i] > k):
			return
		self.heap[i] = k
		while i > 0:
			if i % 2 == 0 and self.heap[i//2 - 1] < self.heap[i]:
				self.heap = self.swap(i,i//2 - 1,self.heap)
				i = (i // 2) - 1
			elif i % 2 == 1 and self.heap[i//2] < self.heap[i]:
				self.heap = self.swap(i,i//2,self.heap)
				i = (i // 2)
			else:
				break

	def insert(self, element):
		# element cannot be smaller than -999999999999999
		self.heap.append(-999999999999999)
		self.increase_key(len(self.heap)-1,element)

	'''
	Returns a sorted array using heap sort based on heap within this class
	'''
	def sorted(self):
		sorted_array = []
		temp_heap = self.heap
		# Loop till array has 1 element
		for i in range(len(self.heap)-1,0,-1):
			self.heap = self.swap(i,0,self.heap)
			maxnum = self.heap[len(self.heap) - 1]
			self.heap.pop(len(self.heap)-1)
			sorted_array.insert(0,maxnum)
			self.max_heapify(0)
		# Insert last element of heap
		sorted_array.insert(0,self.heap[0])
		self.heap = temp_heap
		return sorted_array

	'''
	Returns a sorted array using heap sort in a static method
	'''
	@staticmethod
	def heap_sort(list):
		lst = Heap(list)
		return lst.sorted()






array = [4,1,3,2,16,9,10,14,8,7]

a = Heap(array)
a.insert(8)
a.increase_key(9,20)
print(a)
print(a.sorted())


b = Heap.heap_sort([4,1,3,2,16,9,10,14,8,7])

print(b)
