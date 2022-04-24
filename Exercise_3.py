# Node class  
from platform import node
#Time complexity - O(n)
#space complexity- O(1)


class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):  
        self.data=data
        self.next=None
        
class LinkedList: 
  
    def __init__(self): 
        self.head=None
        self.tail=self.head
        self.length=0

        
  
    def push(self, new_data): 
        #initialize new node
        newnode=Node(new_data)
        #case-1 if list is empty
        if self.head==None:
            self.head=newnode
            self.tail=self.head
        #case-2 if list is not empty
        else:
            #append at the tail
            self.tail.next=newnode
            #set tail as newnode
            self.tail=newnode
        self.length=self.length+1
        
  
    # Function to get the middle of  
    # the linked list 
    #method-1
    def printMiddle(self): 
        current_node=self.head
        middle=self.length//2 #find the middle index
        #traverse until the middle index and return the node.
        for i in range(0,middle):
            current_node=current_node.next
        return current_node.data


    #method-2
    def printMiddle_2(self):
        #initalize two pointers
        slow=self.head  #goes one step
        fast=self.head  #goes two steps
        #loop until fast reaches end of linked-list
        while fast!=None and fast.next!=None:#check both cause(even and odd case,and fast.next.next is being used)
            slow=slow.next
            fast=fast.next.next
        #when fast reaches end , slow will be at middle
        return slow.data

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
print(list1.printMiddle() )
print(list1.printMiddle_2() )
