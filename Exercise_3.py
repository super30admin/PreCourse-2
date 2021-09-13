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
        
        new_node = Node(new_data)
        
        if self.head == None:
            self.head = new_node
            return
        
        p = self.head
        
        while p.next != None:
            p = p.next
            
        p.next = new_node
        
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        
        if self.head is None:
            print("Empty list!")
            return
        
        slow = self.head
        fast = self.head
        
        while (fast.next != None) and (fast.next.next != None):
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