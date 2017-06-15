

class node():
	def __init__(self, cargo, pointer):
		self.cargo = cargo
		self.pointer = pointer

	def hasNextNode():
		if self.pointer:
			return True
		return False

class LinkedList():
	def __init__(self, node):
		self.root_node = node

	def __get_last_node(self):
		passing_node = self.root_node
		while passing_node.hasNextNode():
			passing_node = passing_node.pointer
		return passing_node

	def append(self, node):
		last_node = self.__get_last_node()
		last_node.pointer = node

	def delete_by_cargo(self, cargo):
		passing_node = self.root_node
		prev_passing_node = None
		next_passing_node = None
		while passing_node.hasNextNode() and passing_node.cargo != cargo:
			prev_passing_node = passing_node
			passing_node = passing_node.pointer
			next_passing_node = passing_node.pointer
		prev_passing_node.pointer = next_passing_node