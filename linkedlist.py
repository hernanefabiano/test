#! /usr/bin/python

class ListNode:
	def __init__(self, contents=None, next=None):
		self.contents = contents
		self.next  = next

	def get_cont(self):
		return self.contents

	def __str__(self):
		return str(self.contents)

def print_linked(node):
	print('node:', node)
	while node:        
		print(node.get_cont())
		node = node.next
	print()

def test_list():
	node1 = ListNode("hernan")
	node2 = ListNode("aguilar")
	node3 = ListNode("fabiano")
	node1.next = node2
	node2.next = node3
	print_linked(node1)

if __name__ == "__main__":

	test_list()
