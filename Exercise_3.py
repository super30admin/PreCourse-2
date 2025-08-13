# Node class  
"""
Time Complexity: O(n)
Space Complexity: O(1) --> printMiddle()
"""

class Node:  
    # Function to initialise the node object  
    def __init__(self, data):  
        self.data = data
        self.next = None

  
class LinkedList: 
    def __init__(self): 
        self.head = None
        self.size = 0
        
    def isEmpty(self):
        return self.head is None
    
    def push(self, new_data): # append at the end of list
        new_node = Node(new_data)
        if self.isEmpty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1
        
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
      if self.isEmpty():
          return "List is empty"
      
      slow = self.head
      fast = self.head

      # odd --> middle
      # even --> second middle
      while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
      return f"Second middle if even: {slow.data}"
    
    #   # odd --> middle
    #   # even --> first middle
    #   while fast and fast.next.next:
    #     slow = slow.next
    #     fast = fast.next.next
    #   return f"First middle if even: {slow.data}"


# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.push(0)
print(list1.printMiddle()) 