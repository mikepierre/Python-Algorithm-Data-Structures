class Stack(object):
	def __init__(self):
		self.items = []
		super(Stack, self).__init__()

	def function():
		pass

	def isEmpty(self):
		return self.items == []

	def push(self, item):
		return self.items.append(item)

	def pop(self):
		return self.items.pop()

	def getElements(self):
		return self.items

stack = Stack()
stack.push(1)
stack.push(2)

print stack.getElements()
