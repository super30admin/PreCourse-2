# Node class
# Time Complexity : O(n)
# Space Complexity : O(1)
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList: 
  
    def __init__(self): 
        self.head = None
  
    def push(self, new_data): 
        node = Node(new_data)
        node.next = self.head
        self.head = node
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        print("Input list is")
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next
        fast = slow = self.head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        print("MIDDLE ELEMENT IS")
        print(slow.data)
        return slow.data
# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 
