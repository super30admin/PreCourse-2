# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList: 
  
    def __init__(self): 
        self.head = None
  
    def push(self, new_data): # Time complexity: O(1). Space Complexity: O(1)
        if self.head == None:
            self.head = Node(new_data)
        else:
            new_entry = Node(new_data)
            new_entry.next = self.head
            self.head = new_entry
        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): # Time complexity for this operation is O(n). Space Complexity: O(1)
        if self.head == None: # Handling edge case
            print("LinkedList is empty")
        p1 = self.head
        p2 = self.head
        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next
        print(p1.data)

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
# list1.push(1)
# list1.push(7)
# list1.push(8)
# list1.push(9)
list1.printMiddle() 
