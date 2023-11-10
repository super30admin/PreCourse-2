# Time complexity: o(n)
# space complexity: o(1)
# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):  
        self.data = data
        self.node = None
        
class LinkedList: 
  
    def __init__(self): 
        self.head = None
  
    def push(self, new_data): 
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
        
  
    # Function to get the middle of  
    # the linked list 
    # Here slow pointer and fast pointer approach is used. fast pointer jumps nodes while slow pointer move ahead 
    # by 1 node. When fast pointer eaches the end of the list, slow pointer will be at the middle
    def printMiddle(self): 
        slow_ptr = self.head
        fast_ptr = self.head

        if self.head is not None:
            while (fast_ptr is not None and fast_ptr.next is not None):
                fast_ptr = fast_ptr.next.next
                slow_ptr = slow_ptr.next
            print("The middle element is: ", slow_ptr.data)

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 
