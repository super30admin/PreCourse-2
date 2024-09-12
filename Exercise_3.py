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
        n_node = Node(new_data)
        n_node.next = self.head
        self.head = n_node
        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        s_ptr = self.head
        f_ptr = self.head

        if self.head is not None:
            while(f_ptr is not None and f_ptr.next is not None):
                f_ptr = f_ptr.next.next
                s_ptr = s_ptr.next

            print("The middle element:",s_ptr.data)


# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 
