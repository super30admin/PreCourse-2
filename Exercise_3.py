# Time Complexity : O(N)
# Space Complexity : O(1)
# Did this code successfully run on Leetcode : yes
# Any problem you faced while coding this : no

# Node class  
class Node:
	
    # Function to initialise the node object  
	def __init__(self, data, next=None):
		self.data = data
		self.next = next
        
class LinkedList:
  
	def __init__(self):
		self.head = None


	def push(self, new_data):
		newNode = Node(new_data)
		if self.head is None:
			self.head = newNode
		else:
			newNode.next = self.head
			self.head = newNode

	# Function to get the middle of  
	# the linked list 
	def printMiddle(self):
		slow = self.head
		fast = self.head
		while fast != None and fast.next != None:
			slow = slow.next
			fast = fast.next.next
		print(slow.data)

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(7) 
list1.push(3) 
list1.printMiddle() 
