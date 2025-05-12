# Author : Akaash Trivedi
# Problem : Find Mid Point of a Singly Linked List.
# Time Complexity : O(2n) = O(n)
# Space Complexity : O(1) - no extra memory
# Did this code successfully run on Leetcode : Leetcode #876
# Any problem you faced while coding this : No

# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data, next=None):
        self.data = data
        self.next =  None  
        
class LinkedList: 
  
    def __init__(self): 
        self.head = None
  
    def push(self, new_data): 
        # pushing element at the end of linked list (Like requested in Precourse-1 exercise_3)
        newNode = Node(new_data)
        if self.head is None:
            self.head = newNode
            return self.head
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = newNode
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        if not self.head:
            print("List is empty")
            return
        slow = self.head
        fast = self.head
        while fast and fast.next:
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
