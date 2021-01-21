# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):  
        self.head = data
        self.next = None
        
class LinkedList: 
  
    def __init__(self): 
        self.head =None
  
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
        return
            
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        
        i = self.head
        j = self.head
    
        if self.head != None: 
            while(j.next != None and j != None):
                j = j.next.next
                i = i.next
            print(i.head)
        return
# Driver code 
list1 = LinkedList()
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 
