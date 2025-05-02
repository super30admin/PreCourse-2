"""
Time Complexity

Push : O(n) at the end of the list
Print Middle Element : O(n)

Space Complexity : O(n)
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
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node
        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        count = 0
        curr = self.head
        while(curr):
            count += 1
            curr = curr.next
        midpoint = count // 2
        curr = self.head
        for _ in range(midpoint):
            curr = curr.next
        print(f"Middle Element : {curr.data}")
            

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 
