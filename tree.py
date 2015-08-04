"""
An implementation of a tree structure.
Trees can be constructed independently or given a file 
to create the tree from

Samantha Goldstein
	2015

"""

from node import *


class Tree:


	def __init__(self):
		#Initialize a tree structure
		self.root = None

	def getRoot(self):
		#Accesses root element
		return self.root

	def setRoot(self, root):
		#Sets root element
		self.root = root
		return

	def isEmpty(self):
		#Bool for status of tree
		if self.root == None:
			return True
		else:
			return False


	def makeTree(self, textfl):
		"""
		Creates the tree structure based on input from a file. 
		elements in brackets represent child nodes
		Text File Ex: a[b[cd]ef[g]]
		Represents tree: 

					 a
					/|\
				   b e f
				  /\   |
				 c  d  g

		Parameters:
			textfl: a text file that houses a tree data structure
			tree: an initialized tree structure

		Returns: nothing, -1 if empty file	

		"""

		#Initialization, open file, set vars
		text = open(textfl, "r")
		curr = None
		line = text.readline()


		#Confirm valid file, not empty
		if len(line) == 0:
			return -1

		#Initialize vars
		nd = Node(line[0])
		self.root = nd 
		curr = nd
		place = 1 #will be used to traverse text


		#Traverse text file to set up tree
		while place < len(line):
			#'[' means the following char will represent a child node 
			# so we create a node for the following char, update current node
			if line[place] == '[':
				place += 1 
				nd = Node(line[place], curr)
				curr.addChild(nd)
				curr = nd

			#']' means we've just finished the whole array of children 
			#for an element, so we reset current to a parent element which
			#may still need to add child elements
			elif line[place] == ']':
				curr = curr.getParent()

			#Else we create a node for the char, and set it's parent
			else:
				curr = curr.getParent()
				nd = Node(line[place], curr)
				curr.addChild(nd)
				curr= nd

			place += 1	#update position in text


		return
