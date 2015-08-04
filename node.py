"""
Class Node is a tree node that stores data, a parent, and a list of children

	Samantha Goldstein 2015

"""

class Node:


	def __init__(self, data, parent=None, children=None):
		#setup of default variables. Only need the node's data to construct
		self.data = data 
		if parent is None:
			self.parent = None
		else: 
			self.parent = parent

		if children is None:
			self.children = []
		else:
			self.children = children

	def __str__(self):
		string = self.data + " " + "[ "
		for i in range(len(self.children)):
			string += str(self.children[i]) + ", "
		string +="]"
		return string


	def getData(self):
		return self.data

	def setData(self, data):
		self.data = data
		return 

	def getChildren(self):
		return self.children

	def addChild(self, node):
		self.children.append(node)
		return node

	def getParent(self):
		return self.parent

	def setParent(self, par):
		self.parent = par
		return 



if __name__ == '__main__':
  main()