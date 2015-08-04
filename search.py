"""
This program is an implementation of Depth First Search in Python

	Samantha Goldstein 2015

"""

from node import *
from tree import *
import sys

def main():
	if len(sys.argv) != 2:
		print "Invalid, need two arguments. e.g.\n\t$ python search.py <textfile.txt>"
		return

	filename = sys.argv[1]

	tree = Tree()
	tree.makeTree(filename)
	print "\nLet's Search!"
	find = raw_input("Give me a character to search for: ")
	if len(find)>1:
		print "Sorry that's invalid"
	result = BFS(tree, find)

	if result == -1:
		print "We could not find the element you are looking for. Sorry"
	else:
		print "Found your node! \n" + str(result)



def DFS(tree, item):
	"""
	This is an implementation of depth first search that takes two parameters
		tree: a tree structure to search from
		item: an element to search the tree for

	returns a node if the item is found, else returns -1
	"""

	#Initialize vars
	stack = []
	curr = tree.getRoot()
	stack.append(curr)

	while len(stack)> 0:
		#Pop off the most recently added element
		curr = stack.pop()

		#If the current element is our search item, then return that node
		if curr.getData() == item:
			return curr

		else:
			[stack.append(elem) for elem in curr.getChildren()[-1::-1]]

	return -1
			

def BFS(tree, item):
	"""
	This is an implementation of depth first search that takes two parameters
		tree: a tree structure to search from
		item: an element to search the tree for

	returns a node if the item is found, else returns -1
	"""

	#Initialize vars
	queue = []
	curr = tree.getRoot()
	queue.append(curr)

	while len(queue)> 0:
		#Pop off the most recently added element
		curr = queue[0] #stack.pop()
		queue = queue[1:]
		print curr

		#If the current element is our search item, then return that node
		if curr.getData() == item:
			return curr

		else:
			[queue.append(elem) for elem in curr.getChildren()]

	return -1
	





main()