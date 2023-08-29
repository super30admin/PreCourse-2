#Time Complexity: O(n)
#Space Complexity: O(1)

# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data,next):
        self.data=data
        self.next=None
        
class LinkedList: 
  
    def __init__(self): 
        """
        Create a new singly-linked list.
        Takes O(1) time.
        """
        self.head = None
        self.count=0
        
  
    def push(self, data):
        """
        Insert a new element at the end of the list.
        Takes O(n) time.
        """
        self.count += 1
        if(self.head is None):
            self.head=Node(data=int(data),next=None)
        else:
            temp=Node(data=int(data),next=None)
            travnode=self.head
            # prevnode=travnode
            while(travnode.next is not None):
                
                # prevnode=travnode
                travnode=travnode.next
            travnode.next=temp 
        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        #Takes O(n) time.//
        travnode=self.head
        mid=int(self.count/2)
        i=0
        while(i != mid ):
            
            travnode=travnode.next
            i+=1
        print(travnode.data)
        return

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 
