# Time Complexity : O(n)
# Space Complexity : O(1)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No
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
        
  
    def push(self, new_data): 
        if self.head == None:
            self.head = Node(new_data)
            self.tail = self.head

        else:
            self.tail.next = Node(new_data)
            self.tail = self.tail.next
        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        if self.head == None:
            print("Empty")

        elif self.head.next == None: # Only one element in list
            print(self.head.data)

        else:
            slow, fast = self.head, self.head
            while(fast and fast.next):
                fast = fast.next.next
                slow = slow.next
            print(slow.data)

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 
