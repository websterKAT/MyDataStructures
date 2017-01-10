class Node:
	def __init__(self,data):
		self.data = data
		self.next = None

class linklist:
	def __init__(self):
		self.current = None

	def add(self,data):
		tmp = Node(data)
		tmp.next = self.current
		self.current = tmp	
	
	def addQueue(self):
		queue = []
		p = self.current
		while p != None:
			queue.append(p.data)
			p = p.next
		return queue

	

class graph:
	def __init__(self):
		self.dic = {}
		self.color = {}

	def _add(self,v1,v2):
		if v1 not in self.dic:
			self.dic[v1] = linklist()
		self.dic[v1].add(v2)
		self.color[v1] = 'w'
	
	def add(self,v1,v2):
		self._add(v1,v2)
		self._add(v2,v1)

	def display(self):
		for key , value in self.dic.iteritems():
			print key,"-->"
			value.display()

	def bfs(self):
		queue = []
		queue.append(self.dic.keys()[0])
		while len(queue) != 0:
			tmp = queue.pop(0)
			if self.color[tmp] == 'w':
				print tmp
				self.color[tmp] = 'b'
				p = self.dic[tmp]
				sur = p.current
				while sur != None:
					queue.append(sur.data)
					sur= sur.next



	
g = graph()
g.add(0,1)
g.add(0,5)
g.add(1,2)
g.add(2,3)
g.add(3,4)
g.add(3,5)
g.add(4,0)
g.add(5,4)
g.add(5,2)
g.bfs()


