# Time Complexity : O(n)
# Space Complexity : O(1)


# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data, next = None):  
        self.data = data
        self.next = next
        
class LinkedList: 
  
    def __init__(self): 
        self.dummy = Node(0)
        self.tail = self.dummy

    def push(self, new_data): 
        self.tail.next = Node(new_data)
        self.tail = self.tail.next
        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        head = self.dummy.next
        if not head:
            return
        s,f = head, head
        while (f and f.next):
            f = f.next.next
            s = s.next
        print(s.data)
        
# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 
