class Node:
	def __init__(self,data):
		self.next = None
		self.data = data

class linkedList:
	def __init__(self):
		self.head = None
		self.tail = None
		self.length = 0
	def isEmpty(self):
		return self.head == None

	def size(self):
		return self.length

	def enqueue(self,value):
		newNode = Node(value)
		newNode.next = None
		if self.head == None:
			self.head = newNode
			self.tail = newNode
		else:
			current = self.tail
			current.next = newNode
			self.tail = newNode
		self.length += 1

	def dequeue(self):
		if isEmpty():
			return "cant remove from empty queue"
		else:
			current = self.head
			if  self.head is self.tail:
				self.head = None
				self.tail = None
			else:
				self.head = current.next
			self.length -= 1
			return currnt.data


	def printqueue(self):
		currnt = self.head
		while currnt != None:
			print currnt.data
			currnt = currnt.next
#Jst want to check weather it is working or not

qu = linkedList()
qu.enqueue(23)
qu.enqueue(34)
qu.enqueue(2)
qu.enqueue(4)
qu.enqueue(20)
qu.enqueue(84)
qu.enqueue(78)
qu.enqueue(67)
qu.enqueue(7)
qu.enqueue(19)

qu.printqueue()
