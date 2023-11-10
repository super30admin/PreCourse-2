#-----------------------------------------------------
# Time Complexity : O(n)  ---> n is the number of elements in the array
# Space Complexity : O (n) ---> n is the number of elements in the array
#---------------------------------------------------
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
        # new node
        newNode=Node(new_data)
        # next pointer of new Node
        newNode.next=self.head
        # reset the head pointer
        self.head=newNode


    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 

        if self.head is None:
             print("Empty LinkedList")

        fast=slow=self.head
        # advance slow pointer once and fast pointer twice
        while (fast and fast.next):
            fast=fast.next.next
            slow=slow.next

        print(slow.data)

        
# Driver code 
list1 = LinkedList()
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
# list1.push(1)
list1.printMiddle() 

