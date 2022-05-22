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
        new_node = Node(new_data)   # create a new node
        new_node.next = self.head   
        self.head = new_node
        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        # here we use 2 pointer approach, 1- fast pointer, 2- slow pointer
        fast = self.head        # used to get to the end of the linked list
        slow = self.head        # used to get the middle term

        if self.head is not None:
            while (fast is not None and fast.next is not None):
                fast = fast.next.next
                slow = slow.next
                # for checking
                # print(fast.data, slow.data)
            print("mid point : ",slow.data )


# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 