import unittest

class Stack(list):
	def __init__(self, stack=[]):
		self.extend(stack)
	
	def push(self, item):
		self.insert(0, item)
		return self
	
	def pop(self):
		if self:
			return super(Stack, self).pop(0)
			

class TestStack(unittest.TestCase):
	def test_stack(self):
		stack = Stack()
		self.assertEqual(stack, stack)
		
		stack_items = ['a', 'b', 'c']
		stack = Stack(stack_items)
		self.assertEqual(stack, stack_items)

	def test_push(self):
		stack = Stack()
		stack.push('a')
		self.assertEqual(stack, ['a'])
		stack.push('b')
		self.assertEqual(stack, ['b', 'a'])
	
	def test_pop(self):
		stack = Stack(['a', 'b', 'c'])
		self.assertEqual(stack.pop(), 'a')
		self.assertEqual(stack.pop(), 'b')
		self.assertEqual(stack.pop(), 'c')
		self.assertEqual(stack.pop(), None)


if __name__ == '__main__':
    unittest.main()