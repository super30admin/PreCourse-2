# Time Complexity :O(Log(n))
# Space Complexity :O(1)
# Did this code successfully run on Leetcode : yes I used it in multiple questions on leet code before
# Any problem you faced while coding this : no


# Your code here along with comments explaining your approach
# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):  
        self.next = None
        self.data = data
class LinkedList: 
  
    def __init__(self): 
        self.head = None
        self.end = None
    def push(self, new_data): 
        if self.head == None:
            self.head = Node(new_data)
            self.end = self.head
            return True
        else:
            newNode = Node(new_data)
            self.end.next = newNode
            self.end = self.end.next
            return True
        return False
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        fast = self.head
        slow = self.head
        if not self.head:
            return
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        print(slow.data)

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 
