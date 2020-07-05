# Node class  
""" To find the middle element we have two pointers x and y that initially point to the head of the linkedlist.
Pointer y is advanced by two positions whereas pointer x is advanced by one position. Therefore, x is always halfway before y.
The time complexity for this is O(n) and the space complexity just for the middle element function is O(1) since x and y are simply pointers. """

class Node:
  
	# Function to initialise the node object  
	def __init__(self, data):  
		self.data = data
		self.next = None
		
class LinkedList: 
  
	def __init__(self): 
		self.head = None
  
	def push(self, new_data):
		if(self.head == None):
			self.head = Node(new_data)
			return
		temp = self.head
		while(temp.next != None):
			temp = temp.next
		temp.next = Node(new_data)
		
  
	# Function to get the middle of  
	# the linked list 
	def printMiddle(self): 
		x = self.head
		y = self.head
		while(y!=None):
			if(y.next!=None):
				y = y.next.next
				x = x.next
			else:
				print(x.data)
				return
		if(x!=None):
			print(x.data)
		

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 
