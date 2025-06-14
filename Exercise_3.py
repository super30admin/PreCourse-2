"""
# Time Complexity : 

Node
Init: O(1)

LinkedList

Init: O(1)
Push: O(N)
PrintMiddle: O(N)

# Space Complexity : 
O(N), where N is the number of nodes in the linked list, no auxilliary space

# Did this code successfully run on Leetcode : N/A, performed local testing

# Any problem you faced while coding this : 
> none

"""

# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):  
        self.data = data
        self.next = None
        
class LinkedList: 
  
    def __init__(self):
        self.head = None 
        
  
    def push(self, new_data): 
        newNode = Node(new_data)
        if self.head == None: #could I have checked and set this from None for the first time here itself?
            self.head = newNode
            return
        currNode = self.head
        while currNode.next != None:
            currNode = currNode.next
        currNode.next = newNode

        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        if self.head == None:
            print("None")
            return
        fastNode = self.head
        slowNode = self.head

        while fastNode and fastNode.next:
            fastNode = fastNode.next.next
            slowNode = slowNode.next
        
        print(slowNode.data)

        

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 
