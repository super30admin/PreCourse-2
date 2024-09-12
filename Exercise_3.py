"""
Intuition:  The idea here is increase the 'speed' for traversing a linked list.
This can be done by traversing 2 elements at a time instead of one. 
If we have 2 pointers, we could allow one pointer to traverse at 2x the speed and another at 1x the speed.
If the 2x pointer reaches the end of the linked list, we know that the 1x pointer is at the middle.

Time Complexity : O(N)
Space Complexity : O(1)
"""

class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):  
        self.val = data
        self.next = None
        
class LinkedList: 
  
    def __init__(self): 
        self.head = None
  
    def push(self, new_data):
        #Adding a new node to our linked list
        if self.head == None:
            self.head = Node(new_data)
            return self.head
        pointer = self.head
        while pointer.next != None:
            pointer = pointer.next
        pointer.next = Node(new_data)

        return self.head
    
    def printLL(self):
        pointer = self.head
        while pointer.next != None:
            print("Printed List",pointer.val)
            pointer = pointer.next
        print("Printed List",pointer.val)


    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        #If linked list is empty
        if self.head == None:
            print("Middle None")
            return None

        #If there is only 1 node in linked list
        if self.head.next == None:
            print("Middle", self.head.val)
            return self.head
    
        #If there are multiple nodes
        pointerOne = self.head
        pointerTwo = self.head
        while pointerOne.next != None:
            if pointerOne.next.next != None:
                pointerOne = pointerOne.next.next
                pointerTwo = pointerTwo.next
            else:
                print("Middle", pointerTwo.next.val)
                return pointerTwo.next
        print("Middle", pointerTwo.val)
        return pointerTwo

# Driver code 
list1 = LinkedList() 
list1.push(5) 

list1.push(4)

list1.push(2) 

list1.push(3) 

list1.push(1) 

list1.push(0) 

list1.printMiddle() 
