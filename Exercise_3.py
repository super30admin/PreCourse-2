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
        newNode = Node(new_data)
        newNode.next = self.head
        self.head = newNode 
        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        if self.head is None:
            return None
        slow = self.head
        fast = self.head
        while fast!= None and fast.next !=None:
            slow = slow.next
            fast = fast.next.next

        return slow.data 

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
val=list1.printMiddle() 
print(val)

