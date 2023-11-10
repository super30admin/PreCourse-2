# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):
        self.val = data
        self.next = None  
        
class LinkedList: 
  
    def __init__(self): 
        self.head = None
        
  
    def push(self, new_data):
        new_node = Node(new_data)
        print (new_node)
        new_node.next = self.head
        print(new_node.next)
        self.head = new_node
        print(self.head) 
        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        if not (self.head.next): return self.head
        pMid,pFast = self.head,self.head
        while (pFast and pFast.next):
            pFast = pFast.next.next
            print(pFast,pMid)
            pMid = pMid.next
        return pMid 

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 
