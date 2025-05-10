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
        if not self.head:
            head = new_node
        current = self.head
        while current:
            current = current.next
        current.next = new_node
    
    # Function to get the middle of  
    # the linked list 
    # Approach:
    # 1. Use two pointers: slow_ptr and fast_ptr.
    # 2. Move slow_ptr by 1 node, fast_ptr by 2 nodes each iteration.
    # 3. When fast_ptr reaches the end, slow_ptr will be at the middle.
    def printMiddle(self): 

        slow_ptr = self.head
        fast_ptr = self.head
        
        while fast_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        
        if slow_ptr:
            print(f"The middle element is: {slow_ptr.data}")
        else:
            print("The list is empty.")


# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 
