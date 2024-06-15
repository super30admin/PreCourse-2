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
        if (self.head == None):
           self.head = Node(new_data) 
        else:
            curr = self.head
            while(curr.next is not None):
                curr = curr.next
            curr.next = Node(new_data)
        print(new_data)
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        fast_ptr = self.head
        slow_ptr = self.head
        while(fast_ptr!=None and fast_ptr.next!=None):
            fast_ptr = fast_ptr.next.next
            slow_ptr = slow_ptr.next
        print("Middle element :",slow_ptr.data)
# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 
