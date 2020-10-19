# Node class  
class Node:  
  
    # Function to initialise the node object  
	def __init__(self, data):
		self.data = data
		self.next = None
        
class LinkedList: 
  
	def __init__(self):
		self.head = None
        
  
	def push(self, new_data):
		newnode = Node(new_data) 
		newnode.next = self.head
		self.head = newnode 
        
  
    # Function to get the middle of  
    # the linked list 
	def printMiddle(self):
		slwptr=self.head
		fastptr=self.head

		if self.head is not None:
			while (fastptr is not None and fastptr.next is not None): 
				fastptr = fastptr.next.next
				slwptr = slwptr.next
			print("The middle element is: ", slwptr.data)

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 
