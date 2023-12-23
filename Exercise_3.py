#Time Complexity for pushing into LinkedList is O(n), TC for finding middle is O(n/2) ~ O(n)
# Space Complexity is O(1)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : Not really
# Node class to represent the structure, push and printMiddle methods, 
# In the printMiddle method, used the slow pointer, fast pointer technique, 
# Break the loop of iteration of slow and fast pointer when either the fast pointer is None
# or fast pointer's next is None, depending on if the list has even no of elements or odd.
# After that return slow.
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):
        self.data = data
        self.next = None  
        
class LinkedList: 
  
    def __init__(self):
        self.head = None 
  
    def push(self, new_data):
        nn = Node(new_data)
        if self.head is None:
            self.head = nn
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = nn
        
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        fast = self.head
        slow = self.head
        #If head is single element or None return head
        if self.head is None or self.head.next is None:
            return self.head
        # Break the loop when fast is None or fast.next is None
        # (depending on no of items in the linkedlist if even or odd)
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
        print("middle element is ", slow.data)
    
    def printLinkedList(self):
        curr = self.head
        while curr is not None:
            print(curr.data)
            curr = curr.next

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1)
list1.printLinkedList()
list1.printMiddle() 

# Driver code 
list1 = LinkedList() 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1)
list1.printLinkedList()
list1.printMiddle() 