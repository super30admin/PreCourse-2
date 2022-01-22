# Node class 
# # Time complexity O(n)
# Space complexity O(1) 
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):  
        self.data=data
        self.next=None

class LinkedList: 
  
    def __init__(self): 
        self.head=None
  
    def push(self, new_data): 
#creating a node
        node=Node(new_data)
       #set new node.next to point to head
        node.next=self.head
    # set the head to point to new node
        self.head=node
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
    #using fast and slow pointer initially pointing to head
        slow=self.head
        fast=self.head

        if self.head is not None:
            while (fast is not None and fast.next is not None):
                #fast pointer pointer will be twice ahead of the slow pointer
                fast=fast.next.next
                slow=slow.next
            
            # fast pointerslow pointer reahes to end of the list by then slow pointer will be pointing to the middle of the linked list
            print("middle of linked list: ", slow.data)

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1)
list1.printMiddle() 
