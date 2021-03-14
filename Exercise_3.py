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
        ptr_1=self.head
        ptr_2=self.headv
        d m;ll

        if self.head != None:
            while (ptr_2 != None and ptr_2.next != None):
                ptr_2 = ptr_2.next.next
                ptr_1 = ptr_1.next
            print("The middle element is: ", ptr_1.data)


# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 
