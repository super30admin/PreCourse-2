# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):  
        self.data=data
        self.next_node=None
        
class LinkedList: 
  
    def __init__(self): 
        self.head=None
        
  
    def push(self, new_data): 
        new_node=Node(new_data)  #Inserting data into linked list
        new_node.next_node=self.head
        self.head=new_node
        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        slow_ptr = self.head #pointers pointing to head
        fast_ptr = self.head 
  
        if self.head is not None: 
            while (fast_ptr is not None and fast_ptr.next_node is not None): 
                fast_ptr = fast_ptr.next_node.next_node #fast pointer moves ahead by two nodes
                slow_ptr = slow_ptr.next_node #slow pointer to move by one node. When fast reaches at the end i.e cant move further slow reaches middle
            print("The middle element is: ", slow_ptr.data) 

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 
