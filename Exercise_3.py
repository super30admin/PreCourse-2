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
        if self.head is None:
            self.head=Node(new_data)
        temp=self.head
        while(temp.next):
            temp=temp.next
        temp.next=Node(new_data)
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        #fast pointer will move at twice the speed of slow pointer.
        #so, when fast pointer reaches at the end of linkedlist, slow pointer will be at middle of it.
        slow=self.head
        fast=self.head
        if self.head:
            while fast and fast.next:
                slow=slow.next
                fast=fast.next.next
            print("Middle %d" %slow.data)

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 

#Time Complexity: O(n/2)
#Space complexity: O(1)