class Node:
	def __init__(self,value):
		self.left = None
		self.right = None
		self.data = value

	def __str__(self):
		return str(self.data)

class Tree:
	def __init__(self):
		self.root = None
		

	def insert(self,data):
		if self.root == None:
			self.root = Node(data)

		else:
			current = self.root
			while True:
				if data < current.data:
					if current.left:
						current = current.left
					else:
						current.left = Node(data)
						break
				elif data >= current.data:
					if current.right:
						current = current.right
					else:
						current.right = Node(data)
						break
				else:
					break

	def preOrder(self,node):
		if node is not None:
			print node.data
			self.preOrder(node.left)
			self.preOrder(node.right)
			


	def search(self,data):
		current = self.root
		while True:
			if current is None:
				return False
				break
			elif data == current.data:
				return True
				break
			elif data < current.data:
				current = current.left
			else:
				current = current.right


	def delete(self,data):
		if self.search(data):
			if data == self.root.data:
				current = self.root
				if current.left == None and current.right == None:
					self.root = None
				elif current.left == None and current.right != None:
					self.root = current.right
				elif current.right == None and current.left != None:
					self.root = current.left
				else:
					current1 = current.right
					previous1 = None
					while current1.left is not None:
						previous1 = current1
						current1 = current1.left
					if previous1 == None:
						current.data = current1.data
						if current1.right != None:
							current.right = current1.right
						else:
							current.right = None
					else:
						current.data = current1.data
						if current1.right != None:
							previous1.left = current1.right
						else:
							previous1.left = None

			else:
				current = self.root
				previous = None
				found = False
				while found != True:
					if data == current.data:
						found = True
						break
					elif data < current.data:		
						previous = current
						current = current.left
					else:
						previous = current
						current = current.right
			
				if current.left == None and current.right == None:
					if previous.left == current:
						previous.left = None
					else:
						previous.right = None
			
				elif (current.left == None and current.right != None):
					if previous.left == current:
						previous.left = current.right
					else:
						previous.right = current.right

				elif(current.right == None) and (current.left != None):
					if previous.left == current:
						previous.left = current.left
					else:
						previous.right = current.left
				else:
					current1 = current.right
					previous1 = None
					while current1.left is not None:
						previous1 = current1
						current1 = current1.left
						current.data = current1.data
					if previous1 == None:
						current = current1.data
						if current1.right != None:
							current.right = current1.right
						else:
							current.right = None

					elif current1.left == None and current1.right == None:
						current.data = current1.data
						if previous1.left == current1:
							previous1.left = None
						else:
							previous1.right = None
					else:
						current.data = current1.data
						if previous1.left == current1:
							previous1.left = current1.right
						else:
							previous1.right = current1.right

					
				
		else:
			print "This value doesnt exist"





t = Tree()
t.insert(100)
t.insert(200)
t.insert(100)
t.insert(500)
t.insert(100)
t.insert(600)
t.delete(100)


t.preOrder(t.root)
