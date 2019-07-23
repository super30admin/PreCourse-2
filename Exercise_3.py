class LinkedList:
	class Node:
		def __init__(self, dataval=None):
			self.data = dataval
			self.next = None

	def __init__(self):
		self.head = None

	def printMiddle(self):
		fast = self.head
		slow = self.head
		if self.head != None:
			while fast != None and fast.next != None:
				fast = fast.next.next
				slow = slow.next
			print("Element present at the middle of the linked list is", slow.data)

	def push(self, new_data):
		new_node = self.Node(new_data)
		new_node.next = self.head
		self.head = new_node

	def printList(self):
		temp = self.head
		print("LinkedList is :")
		while temp != None:
			print(str(temp.data) + "->", end = "")
			temp = temp.next
		print("NULL")

if __name__ == "__main__":
	llist = LinkedList()
	for i in range(15, 0, -1):
		llist.push(i)
		llist.printList()
		llist.printMiddle()