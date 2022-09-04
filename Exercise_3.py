#Time-Complexity: O(n)
#Space-Complexity: O(n)

#Node class  
from email import header


class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):  
        self.data=data
        self.next=None

class LinkedList: 
  
    def __init__(self): 
        self.head=None
  
    def push(self, new_data): 
        node = Node(new_data)
        current=self.head
        if self.head is None:
            self.head = node

        else:
            while current.next!=None:
                current=current.next   
            current.next=node

    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        current=self.head
        length=0
        while current is not None:
            current=current.next
            length+=1
        
        current = self.head 
        mid=0
        while (mid<length//2):
            current=current.next
            mid+=1

        return current.data

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
print("The middle element is",list1.printMiddle())
