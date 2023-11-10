# Time Complexity : Push - O(1), PrintMiddle - O(1)
# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data): 
        self.val = data
        self.next = next
        
class LinkedList: 
    "Linked List Class"
    def __init__(self): 
        self.head = None
        self.tail = None
        self.size = 0
  
    def push(self, new_data): 
        if self.head:
            newtail = Node(new_data)
            self.tail.next = newtail
            self.tail = newtail
        else:
            self.head = Node(new_data)
            self.tail = self.head
        self.size += 1
        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        mid = (self.size // 2) 
        count = 0
        self.fakehead = self.head

        while count < mid:
            self.fakehead = self.fakehead.next
            count += 1
        
        print(self.fakehead.val)


# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 
