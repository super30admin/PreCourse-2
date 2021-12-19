#  Time Complexity : O(n)
#  Space Complexity : O(1) as we are using 2 variables.
#  Did this code successfully run on Leetcode : Yes
#  Any problem you faced while coding this : No
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
        if(self.head == None):
            self.head = Node(new_data)
        else:
            current = self.head
            while(current.next != None):
                current = current.next
            current.next = Node(new_data)
        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        i = self.head
        j = self.head
        # use 2 variables. i jumps 2 steps and j jumps 1 step each time till the end of the linked list.
        while(i and i.next != None and i.next.next != None):
            i = i.next.next
            j = j.next
        print(j.data)

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 
