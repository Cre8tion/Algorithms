class Node:
	def __init__(self,key):
		self.left_node = None
		self.right_node = None
		self.val = key



class Tree:
	def __init__(self):
		self.root = None

	def add(self,key):
		
		if self.root == None:
			self.root = key

