import unittest

class Queue(list):
	'''
	Data structure definition 
	'''
	def __init__(self, queue=[]):
		self.queue = queue
	
	def enqueue(self, item):
		'''
		adds item to the queue as index -1
		return queue
		'''
		self.queue.append(item)
		return self.queue

	def dequeue(self):
		'''
		remove item at 0 and return its
		'''
		if self.queue:
			return self.queue.pop(0)


class TestQueue(unittest.TestCase):
	def test_enqueue(self):
		queue = Queue()
		self.assertEqual(queue.enqueue("a"),["a"])

	def test_dequeue(self):
		queue = Queue(["a","b","c"])
		self.assertEqual(queue.dequeue(), "a")
		self.assertEqual(queue.queue, ["b","c"])

		queue = Queue([])
		self.assertEqual(queue.dequeue(), None)

	def test_init(self):
		queue_list = ["a","b","c"]
		queue = Queue(queue_list)
		self.assertEqual(queue.queue, queue_list)

if __name__ == '__main__':
    unittest.main()