# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):  
    	self.data=data
    	self.next=None
        
class LinkedList: 
  
    def __init__(self): 
    	self.head=None
  
    def push(self, new_data):
    	if self.head==None:
    		self.head=Node(new_data)
    	else:
    		temp=self.head
    		while temp.next!=None:
    			temp=temp.next
    		temp.next=Node(new_data)

    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
    	pre=temp=self.head
    	while temp and temp.next:
    		pre=pre.next
    		temp=temp.next.next
    	print(pre.data)



# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 
