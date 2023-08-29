# Time Complexity : O(n) for finding middle node
#  Space Complexity : O(n)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):  
        self.data = data
        self.next = None
        
class LinkedList: 
  
    def __init__(self):
        self.head =None 
        self.tail = None
        
  
    def push(self, new_data): 
        if self.head is None:
            self.head = self.tail = Node(new_data)
        else:
            self.tail.next = Node(new_data)
            self.tail = self.tail.next

        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        if self.head is None: 
            print("No middle node")
            return
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
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
