'''
Time Complexity : O(n) for finding middle. push is 0(1) since we are using tail pointer.
Space Complexity : O(1).
Did this code successfully run on Leetcode : Yes (#872)
Any problem you faced while coding this : NO.
Approach:
Tried iterative findLength approach and later used slow & fast pointer pattern approach to further optimize.
'''
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
        newNode = Node(new_data)
        if not self.head:
            self.head = newNode
            self.tail = newNode
            return
        prevNode = self.tail
        self.tail = newNode
        prevNode.next = self.tail

    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        findMiddleNode = self._findMiddle()
        # findMiddleNode = self._fastSlowPointerApproach()
        print("Middle node", findMiddleNode.data)

    def _findLength(self):
        tmpNode = self.head
        length = 0
        while tmpNode:
            length+=1
            tmpNode = tmpNode.next
        return length
    
    def _findMiddle(self):
        lengthOfList = self._findLength()
        middle = lengthOfList//2
        tmpNode = self.head
        while middle!=0:
            middle-=1
            tmpNode = tmpNode.next
        return tmpNode

    def _fastSlowPointerApproach(self):
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

# Driver code 
list1 = LinkedList()
list1.push(5)
list1.push(4)
list1.push(2) 
list1.push(3)
list1.push(1)
list1.printMiddle()