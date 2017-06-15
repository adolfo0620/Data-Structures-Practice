import unittest

class Stack(list):
	def __init__(self, stack=[]):
		self.extend(stack)
	
	def push(self, item):
		self.insert(0, item)
	
	def pop(self):
		if self:
			self.pop(0)

class TestStack(unittest.TestCase):
	def test_stack(self):
		pass
	
	def test_push(self):
		pass
	
	def test_pop(self):
		pass