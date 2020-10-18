# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data): 
        self.data = data
        self.next = None 
        
class LinkedList: 
  
    def __init__(self): 
        self.root = None
        
  
    def push(self, new_data): 
        newNode = Node(new_data)
        newNode.next = self.root
        self.root = newNode
        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        slow = self.root
        fast = self.root
        if self.root is not None:
            while fast is not None and fast.next is not None:
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
print(list1.printMiddle())
