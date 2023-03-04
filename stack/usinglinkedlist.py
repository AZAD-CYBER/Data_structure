#  Stack Node
class StackNode:
	def __init__(self, data, top):
		self.data = data
		self.next = top


class MyStack:
	def __init__(self):
		self.top = None
		self.count = 0

	#  Returns the number of element in stack
	def size(self):
		return self.count

	def isEmpty(self):
		if (self.size() > 0):
			return False
		else:
			return True

	#  Add a new element in stack

	def push(self, data):
		#  Make a new stack node
		#  And set as top
		self.top = StackNode(data, self.top)
		#  Increase node value
		self.count += 1

	#  Add a top element in stack
	def pop(self):
		temp = 0
		if (self.isEmpty() == False):
			#  Get remove top value
			temp = self.top.data
			self.top = self.top.next
			#  Reduce size
			self.count -= 1

		return temp

	#  Used to get top element of stack
	def peek(self):
		if (not self.isEmpty()):
			return self.top.data
		else:
			return 0
	def display(self):
		while self.top!=None:
			print(self.top.data)
			self.top=self.top.next

	#  Create new stack        +  
s = MyStack()
print("\n Is empty : ", s.isEmpty())
	#  Add element
s.push(15)
s.push(14)
s.push(31)
s.push(21)
s.push(10)
print("\n Top  : ", s.peek())
print(" Size : ", s.size())
print("\n Is empty : ", s.isEmpty())
	#  Delete Stack Element
# data = s.pop()
# print("\n Pop element ", data)
print(" Size : ", s.size())
# data = s.pop()
# print("\n Pop element ", data)
print(" Size : ", s.size())
# s.pop()
s.display()



    
