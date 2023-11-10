# Node class
# Time complexity: O(n)
# Space complexity: O(1) 
class Node:
    def __init__(self, data=0,next=None):
        self.data=data
        self.next=next  
        
class LinkedList: 
    def __init__(self): 
        self.head=None
  
    def push(self, new_data):
        if not self.head:
            self.head=Node(new_data)
        else:
            curr=self.head
            while curr.next:
                curr=curr.next
            curr.next=Node(new_data)

        
    def printMiddle(self):
        slow,fast=self.head,self.head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        print(slow.data) 

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 
