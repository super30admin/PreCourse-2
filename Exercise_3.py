#Space complexity  and time  complexity  is O(n) 
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
        slow_pointer = self.head
        fast_pointer = self.head
        if self.head is not None:
            while fast_pointer is not None and fast_pointer.next is not None:
                slow_pointer = slow_pointer.next
                fast_pointer = fast_pointer.next.next
            print("The middle element is: ", slow_pointer.data)
        else:
            print("The list is empty")

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(88) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 
