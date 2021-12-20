# Time Complexity:
    # push: O(1)
    # printmiddle: O(n)
# Space Complexity: O(n)
# Did this code successfully run on Leetcode: Yes
# Any problem you faced while coding this: No

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
        if self.head == None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node
        return
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        curr = self.head
        size = 0
        while curr != None:
            size += 1
            curr = curr.next
        mid = size//2
        curr2 = self.head
        while mid:
            curr2 = curr2.next
            mid -= 1
        print("The Mid Element is", curr2.data)
        return

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 
