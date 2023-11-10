# Linked_list Time Complexity, best case:O(1), worst, avg case:O(n)
# Linked_list Space Complexity, best case: O(1), worst case: O(n)

# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):  
        #creating and initializing a node with the data and next fields
        self.data=data
        self.next=None
        
class LinkedList: 
    # initializing the head node 
    def __init__(self): 
        self.head=None
  
    def push(self, new_data): 
        newNode=Node(new_data)
        #if linkedlist is empty adding the new node as the head node 
        if self.head==None:
            self.head=newNode
        else:
        #adding new node at the beginning of the linked list
            newNode.next=self.head
            self.head=newNode
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        #getting to the middle of the linked list with the help of two pointers slow and fast
        fast=slow=self.head
        while fast.next!=None:
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
