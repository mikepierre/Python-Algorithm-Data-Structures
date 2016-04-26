class stack(object):
	def __init__(self, limit = 10):
		super(stack, self).__init__()
		self.stk = []
		self.limit = limit
		#self.arg = arg

	def isEmpty(self):
		return len(self.stk) <= 0

	def push(self, item):
		if len(self.stk) >= self.limit:
			print "Stack overflow"
		else:
			self.stk.append(item)
			print self.stk

	def pop(self):
		if len(self.stk):
			print "Stack Underflow"
			return 0
		else:
			return self.stk.pop()

	def peek(self):
		if len(self.stk) <= 0:
			print "stack underflow"
			return 0
		else:
			return self.stk[-1]

	def size(self):
		return self.stk(self.stk)

the_stack = stack(5)
the_stack.push("1")
the_stack.push("2")
the_stack.push("99")
print the_stack.peek()
print the_stack.pop()
