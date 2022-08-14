#Time Complexity : O(n)
 #Space Complexity : O(n)
 #Did this code successfully run on Leetcode :
 #Any problem you faced while coding this :

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
        node = Node(new_data)
        if self.head is None:
            self.head = node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = node
            
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        if self.head is None:
            print("No elements is LinkedList")
        if self.head.next.next is None:
            print("Only two elements in Linked list, cannot find middle")
        else:
            fast_pointer = self.head
            slow_pointer = self.head
            while fast_pointer.next:
                fast_pointer = fast_pointer.next.next
                slow_pointer = slow_pointer.next
            print("Middle element is: ", slow_pointer.data)

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 
