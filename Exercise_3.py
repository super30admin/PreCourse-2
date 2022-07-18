"""
Exercise_3 : Find Mid Point of a Singly Linked List.
Time Complexity : O(N)
    
Space Complexity : O(1) 


Two Pointers is used to find the middle Node

During each iteration:
    First Pointer moves one Node at a time
    Second Pointer moves jumps two nodes
    
When the second Node reached the last node, the node that the First pointer is pointing to 
will be the Middle Node

@name: Rahul Govindkumar_RN27JUL2022
"""

# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data): 
        self.data = data
        self.next = None
        
class LinkedList: 
  
    def __init__(self): 
        self.head =None
        
  
    def push(self, new_data): 
        
        newNode= Node(new_data)
        
        if self.head ==None:            
            self.head=newNode
            return
        
        else:
            lastNode= self.head
            
            while (lastNode.next):
                lastNode = lastNode.next
            
            lastNode.next=newNode
            return
            
            
        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        
        self.printList()
        
        p1=self.head
        p2=self.head
        
        while p2 and (p2.next):
            p1=p1.next
            p2=p2.next.next
 
        print("\nThe Middle value is ",p1.data)            
            
        
    def printList(self): 
        
        lastNode= self.head
            
        while (lastNode):
            print(str(lastNode.data) + "->", end="")
            lastNode = lastNode.next
        print("Null")

        

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1)
list1.push(0)  
list1.printMiddle() 
