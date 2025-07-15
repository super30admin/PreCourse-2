#Find the middle of a linked list
# Time Complexity: O(n)
# Space Complexity: O(1)
# Did this code successfully run on Leetcode : Yes(876)
# Any problem you faced while coding this : None


# Node class  
class Node:
    
  
    # Function to initialise the node object  
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList: 
  
    def __init__(self):
        self.head = None
    # Inserts a new node at the beginning of the list
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
        
  
    # Function to get the middle of the linked list 
    def printMiddle(self):
        s = f = self.head
        while f and f.next:
            s = s.next  #Slow pointer
            f = f.next.next #Fast pointer
        print(s.data)
        

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 
