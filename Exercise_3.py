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
        newnode=Node(new_data)
        newnode.next=self.head
        self.head = newnode
        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        lptr=self.head
        rptr=self.head

        if self.head is not None:
            while(rptr is not None and rptr.next is not None):
                rptr=rptr.next.next
                lptr=lptr.next
            print("Mid Element: ",lptr) 

if __name__=='__main__': 
    # Driver code 
    list1 = LinkedList() 
    list1.push(5) 
    list1.push(4) 
    list1.push(2) 
    list1.push(3) 
    list1.push(1) 
    list1.printMiddle() 
