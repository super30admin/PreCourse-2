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
        node =  Node(new_data)
        if self.head == None:
            self.head = node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = node

    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        slow_ptr = self.head
        fast_ptr = self.head
        while fast_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr =  fast_ptr.next.next
        if slow_ptr:
            print(slow_ptr.data)
        else:
            print("the linked list is empty")


# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 
