class Node():
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList():
	def __init__(self):
		self.head = None

	def push(self, data): 
		new_node = Node(data)
		new_node.next = self.head
		self.head = new_node

	def append(self,data):
		new_node = Node(data)
		if self.head == None:
			self.head = new_node
		else:
			current = self.head
			while current.next:
				current = current.next
			current.next = new_node

	def length(self):
		current = self.head
		count = 0
		while current:
			count += 1
			current = current.next
		return count

	def printLinkedList(self):
		current = self.head
		print("The LinekedList is: ")
		while current:
			print(current.data)
			current = current.next
	
	def printMiddle(self):
		if self.head == None:
			print("List is empty")
		slow = self.head
		fast = self.head
		while fast and fast.next:
			slow = slow.next
			fast = fast.next.next
		print("Middle of the Linked List is %d"%slow.data)



''' Driver Code '''
ll = LinkedList()
ll.push(10)
ll.push(9)
ll.push(8)
ll.push(7)
ll.push(6)
ll.push(5)
ll.push(4)
ll.push(3)
ll.push(2)
ll.push(1)
ll.push(0)
ll.printLinkedList()
ll.printMiddle()
