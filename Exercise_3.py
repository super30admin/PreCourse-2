# Node class
#Find Mid Point of a Singly Linked List python
# Time complexity: O(n)
# Space Complexity: O(1)
# Difficulty faced in logic.

class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):               #Node contains data and next ref
        self.data = data
        self.next= None

class LinkedList:

    def __init__(self):                     #Linked List contains nodes, first node will be head
        self.head = None
  
    def push(self, new_data):               #push and link between nodes
        new_node= Node(new_data)
        new_node.next= self.head
        self.head= new_node
        print(self.head.data)
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):                  #Slow-Fast 2 pointer logic, Fast pointer will jump 2x as of slow pointer, we will iterate till fast pointer reaches at the end.
        slow= self.head
        fast= self.head

        if self.head is not None:
            while fast is not None and fast.next is not None:
                fast = fast.next.next
                slow = slow.next
        print("Middle element is :", slow.data)     #Print slow pointer data..which will ultimately be at middle


# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 
