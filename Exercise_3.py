# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):  
        self.data = data
        self.next = None
        
class LinkedList: 
  
    def __init__(self): 
        self.head = None
        self.cur = None
        
  
    def push(self, new_data):
        #Insert at the end O(1)
        node = Node(new_data)
        if self.head:
            self.cur.next = node    
        else:
            self.head = node
        self.cur = node
        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        # prints the middle left element when No of elements are even.
        fast = self.head
        slow = self.head

        while fast and fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        print(slow.data)


# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 
