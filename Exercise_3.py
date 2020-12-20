#Returning left of middle 2 element if linked list has even numbered elements
# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data): 
        self.data = data 
        self.next = None
        
class LinkedList: 
  
    def __init__(self): 
        self.head = None
  
    def push(self, new_data): #O(n) = 1
        ptr = self.head
        if not ptr:
            self.head = Node(new_data)
            return
        while ptr.next:
            ptr = ptr.next
        ptr.next = Node(new_data)
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): #O(n) = n
        if not self.head:
            print("Empty list")
            return
        slow_ptr = self.head
        fast_ptr = self.head
        while fast_ptr.next and fast_ptr.next.next:
            fast_ptr = fast_ptr.next.next
            slow_ptr = slow_ptr.next

        print(slow_ptr.data)

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.push(0) 
list1.push(-1) 
list1.printMiddle() 
