# Time Complexity : O(n)
# Space Complexity : O(1)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No problem, just used the two pointers

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
        if self.head is not None:
            curr = self.head

            while curr.next is not None:
                curr = curr.next

            curr.next = Node(new_data)

        else:
            self.head = Node(new_data)
        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        '''
        p1 moves one node at a time
        p2 moves two nodes at a time
        When the p2 reaches to the end of the linked list, p1 is at the middle node.
        If there are 2 middle nodes, then the p1 will be at the second middle node. (Requirement by leetcode)
        odd is the pointer next to the p2.
        even is the next to odd which will be the next position of p2.
        '''
        p1 = self.head
        p2 = self.head.next

        if p1 is None or p2 is None:
            return p1.data
        
        while True:
            p1 = p1.next
            odd = p2.next

            if odd is None:
                return p1.data
            
            even = p2.next.next
            if even is None:
                return p1.data
            
            p2 = even

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
print(list1.printMiddle()) 
