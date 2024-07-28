# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):  
        self.data=data
        self.next=None
class LinkedList: 
  
    def __init__(self): 
        self.head=None
        
  
    def push(self, new_data): 
        node=Node(new_data)
        if self.head is None:
            self.head=node
        else:
            cur=self.head
            while cur.next:
                cur=cur.next
            cur.next=node
        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        cur=self.head
        slow=fast=cur
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow.data

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 

print(list1.printMiddle()) 

print("Middle of the linked list is:", list1.printMiddle())