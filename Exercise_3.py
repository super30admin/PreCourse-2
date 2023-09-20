# Exercise_3 : Find Mid Point of a Singly Linked List.
# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):
        self.data = data
        self.next = None 
        
class LinkedList: 
  
    def __init__(self): 
        self.head = None
        self.temp = None
  
    def push(self, new_data):
        # when list is empty
        # make head point to first node
        # temp point to first node
        if self.head is None:
            n = Node(new_data)
            self.head = n
            self.temp = self.head

        # temp helps linking new node to list
        else:
            n = Node(new_data)
            self.temp.next = n
            self.temp = self.temp.next
 
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        slow = self.head
        fast = self.head.next

        # slow goes at 1 hop each, fast goes 2 times the slow hop,
        # until fast reaches the end of list
        # slow is at the middle of list
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
