#! /usr/bin/python

class BinaryTree():

	def __init__(self,root):
		self.left = None
		self.right = None
		self.root = root

	def get_left_data(self):
		return self.left

	def get_right_data(self):
		return self.right

	def set_node(self,value):
		self.root = value
	
	def get_node(self):
		return self.root

	def set_right(self,newNode):
		if self.right == None:
			self.right = BinaryTree(newNode)
		else:
			tree = BinaryTree(newNode)
			tree.right = self.right
			self.right = tree

	def set_left(self,newNode):
		if self.left == None:
			self.left = BinaryTree(newNode)
		else:
			tree = BinaryTree(newNode)
			self.left = tree
			tree.left = self.left

def print_structure(tree_struct):

	if tree_struct
		print_structure(tree_struct.get_left_data())
		print(tree_struct.get_node())
		print_structure(tree_struct.get_right_data())

def testData():
	_tree = BinaryTree("hernan")
	_tree.set_left("aguilar")
	_tree.set_right("fabiano")
	_tree.set_right("junior")
	print_structure(_tree)

if __name__ == "__main__":

	testData()