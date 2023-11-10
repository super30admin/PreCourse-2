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
        if self.head == None:
            self.head = Node(new_data)
        else:
            ptr = self.head
            nxtnode = Node(new_data)
            while ptr.next != None:
                ptr = ptr.next
            ptr.next = nxtnode
  
    # Function to get the middle of  
    # the linked list 
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
