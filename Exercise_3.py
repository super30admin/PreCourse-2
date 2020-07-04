# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):  
        self.val = data
        self.next = None
        
class LinkedList: 
  
    def __init__(self):
        self.head = None
          
    def push(self, new_data): 
        if not self.head:
            self.head = Node(new_data)
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = Node(new_data)
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
    	slow, fast = self.head, self.head
    	while fast and fast.next:
    		slow = slow.next
    		fast = fast.next.next
    	print(slow.val)

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 
