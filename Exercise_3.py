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
        new_n = Node(new_data)
        new_n.next = self.head
        self.head = new_n

    # Function to get the middle of  
    # the linked list 
    # using the concept of tortoise and hare or slow or fast pointers
    def printMiddle(self): 
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        print(slow.data)

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 
