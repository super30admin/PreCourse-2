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
        # Time O(n) , we can optimize this if we maintain a tail pointer
        # space O(1) for new Node
        n = Node(new_data)
        if not self.head:
            self.head = n
        else:
            p = self.head
            while p.next:
                p = p.next
            p.next = n
  
    def print(self):
        # Time O(n)
        # space O(1)
        p = self.head
        while p:
            print(p.data)
            p = p.next

    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        # Time O(n)
        # space O(1)
        p1 = p2 = self.head
        while p1 and p1.next:
            p1 = p1.next.next
            if p1:
                p2 = p2.next
        print(p2.data)
    
    def printMiddleTwoPass(self):
        # Time O(n)
        # space O(1)
        size = 0
        p = self.head
        while p.next:
            size += 1
            p = p.next
        mid = size // 2
        p = self.head
        while mid > 0:
            p = p.next
            mid -= 1
        print(p.data)

# Driver code 
list1 = LinkedList() 
for i in range(16):
    list1.push(i+1)
# list1.print()
list1.printMiddle() 
list1.printMiddleTwoPass()
