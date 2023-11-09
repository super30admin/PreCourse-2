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
        inp=Node(new_data)
        if self.head==None:
            self.head=inp
        else:
            temp=self.head
            while temp.next!=None:
                temp=temp.next
            temp.next=inp
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        if self.head!=None:
            fast=self.head
            slow=self.head
            while fast.next!=None:
                slow=slow.next
                fast=fast.next.next
            print(slow.data)
            return slow.data

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 
