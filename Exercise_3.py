# Node class  
#Time complexity O(n)
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):
        self.data=data
        self.next=None 
        
class LinkedList: 
  
    def __init__(self):
        self.head=None

    def push(self, new_data):
        n=Node(new_data)
        n.next=self.head
        self.head=n
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        s=self.head
        f=s
        while f and f.next:
            s=s.next
            f=f.next.next
        print(s.data)

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1)
list1.push(0)
list1.push(10) 
list1.push(11)
list1.printMiddle() 
