
"""
Time complexity : O(n)
Space Complexity: O(n)

The time complexity is O(n) because we need to  
loop through the node
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
        self.tail = None
        self.length = 0
        
  
    def push(self, new_data): 
        new_node = Node(new_data)
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        
    def get(self, index):
        temp = self.head
        if index < 0 or index >= self.length:
            return None
        else:
            for _ in range(index):
                temp = temp.next
            return temp.data
        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        if self.length == 0:
            return None
        elif self.length == 1:
            return self.head.data 
        else:
            mid = self.length // 2
            return self.get(mid)
        

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
#list1.push(1) 
print(list1.printMiddle())
