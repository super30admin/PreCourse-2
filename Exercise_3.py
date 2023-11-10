# Time Complexity : O(N)
# Space Complexity : O(1)

# Exercise 3 : Find Mid Point of a Singly Linked List
# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):  
        self.data = data
        self.next = None
        
class LinkedList: 
  
    def __init__(self): 
        self.head = None
        
    #code to push nodes on the Linked LIst
    def push(self, new_data): 
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        slow = self.head
        fast = self.head
        #we are using two pointer approach, and we advance fast pointer by 2, and slow pointer by 1. By the time the fast pointer reaches the end,
        #the slow pointer will reach the middle of the linked list
        if self.head is not None:
            while(fast is not None and fast.next is not None):
                fast = fast.next.next
                slow = slow.next
            print("The middle element is: ", slow.data)

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 
