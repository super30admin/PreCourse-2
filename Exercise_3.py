# Time Complexity : push O(n), printMiddle O(n)
# Space Complexity : push O(1), printMiddle O(1) - only really storing head variable
# Did this code successfully run on Leetcode : yes
# Any problem you faced while coding this : No, but remember to increment/decrement mid index

# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):  
        self.data = data
        self.next = None
        
class LinkedList: 
  
    def __init__(self): 
        self.head = None
        self.count = 0
  
    def push(self, new_data): 
        newNode = Node(new_data)
        self.count += 1
        
        if self.head is None:
            self.head = newNode
            return
       
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        curr.next = newNode
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        if self.head is None:
            print("Empty list")
            return
        
        midIndex = self.count//2

        i = 0
        current = self.head
        while i < midIndex:
            current = current.next
            i += 1
        print(current.data)

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.push(1) 
list1.printMiddle() 
