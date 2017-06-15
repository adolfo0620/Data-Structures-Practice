import unittest

class Node():
	def __init__(self, cargo, pointer):
		self.cargo = cargo
		self.pointer = pointer

	def has_next_node(self):
		if self.pointer:
			return True
		return False

class LinkedList():
	def __init__(self, node):
		self.root_node = node

	def __get_last_node(self):
		passing_node = self.root_node
		while passing_node.has_next_node():
			passing_node = passing_node.pointer
		return passing_node

	def does_contain(self, node):
		passing_node = self.root_node
		if passing_node == node:
				return True

		while passing_node.has_next_node():
			if passing_node == node:
				return True
			passing_node = passing_node.pointer
		
		return False

	def append(self, node):
		last_node = self.__get_last_node()
		last_node.pointer = node

	def delete_by_cargo(self, cargo):
		passing_node = self.root_node
		prev_passing_node = None
		next_passing_node = None
		while passing_node.has_next_node() and passing_node.cargo != cargo:
			prev_passing_node = passing_node
			passing_node = passing_node.pointer
			next_passing_node = passing_node.pointer
		prev_passing_node.pointer = next_passing_node


class TestLinkedList(unittest.TestCase):
	def test_get_last_node(self):
		node = Node('first', Node)
		linkedList = LinkedList(node)
		self.assertEqual(linkedList.root_node, node)

	def test_append(self):
		root_node = Node('first', None)
		second_node = Node('second', None)
		linkedList = LinkedList(root_node)
		linkedList.append(second_node)
		self.assertEqual(linkedList.root_node.pointer, second_node)
		self.assertEqual(linkedList.root_node.pointer.cargo, second_node.cargo)

	def test_does_contain(self):
		node = Node('first', Node)
		linkedList = LinkedList(node)
		self.assertTrue(linkedList.does_contain(node))
		
	def test_delete_by_cargo(self):
		root_node = Node('first', None)
		second_node = Node('second', None)
		linkedList = LinkedList(root_node)
		linkedList.append(second_node)
		linkedList.delete_by_cargo(second_node.cargo)
		self.assertFalse(linkedList.does_contain(second_node))

class TestNode(unittest.TestCase):
	def test_node(self):
		node = Node("first", None)
		self.assertEqual(node.cargo, "first")
		self.assertEqual(node.pointer, None)

	def test_has_next_node(self):
		node = Node("first", None)
		self.assertFalse(node.has_next_node())

		node.pointer = Node("second", None)
		self.assertTrue(node.has_next_node())

if __name__ == '__main__':
    unittest.main() 