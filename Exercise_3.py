"""
Runtime Complexity:
-O(n), as we need to traverse the entire list using two pointers slow and fast. We increment slow by one whereas fast by two, in this case the slow will reach the middle 
element of the list whereas the fast gets stopped at the last element of the list.
-O(1) - push() operation, as we add a node to the front of the list by changing the next pointers and head.

-Yes, the code worked on leetcode
- I wanted to make sure the order in which the elements are added to the list. So, I created a extra function to print the items in the list to make sure my solution was right.
"""

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
        new_node.next = self.head
        self.head = new_node
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        slow = fast= self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 
        print("\n")
        print("The middle element of the list is: "+ str(slow.data))
    
    def printList(self):
        result =[]
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
        
        
        
        

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printList()

list1.printMiddle() 
