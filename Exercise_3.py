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
        idx1 = self.head;
        idx2 = self.head

        while idx2 != None and idx2.next != None:
            idx1 = idx1.next
            idx2 = idx1.next.next
        
        print("The middle element is :",idx1.data)



# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 
