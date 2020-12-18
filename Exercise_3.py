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
             self.head = Node(new_data)
             return
        newnode=Node(new_data)
        newnode.next=self.head
        self.head=newnode

        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
      count=0
        i=self.head
        while i.next is not None:
            count=count+1
            i=i.next
        c=count//2
        i=self.head
        n=0
        while n<c:
            i=i.next
            n=n+1
        print("midpoint is:",i.data)


# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 
