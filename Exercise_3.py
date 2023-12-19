# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):  
        self.data = data
        self.next = None

## Time complexity : O(n)
## Space complexity : O(1)
        
class LinkedList: 
  
    def __init__(self): 
        self.head = None
        
  
    def push(self, new_data): 
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
        
    #Foolowing algorithm ensures that the middle element is found always, in case of even number of nodes, it prints second node    
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        sp = self.head
        fp = self.head

        if self.head is not None:
            while fp is not None and fp.next is not None:
                fp = fp.next.next
                sp = sp.next

            print("Middle element: ", sp.data)

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 
