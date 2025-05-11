# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data=None, nxt=None): 
        self.data = data
        self.nxt = nxt
        
class LinkedList: 
    __slots__='head','size'
    head:Node
    size:int
  
    def __init__(self): 
        self.head = None
        self.size = 0
        
  
    def push(self, new_data): 
        new_node = Node(new_data)
        if self.head is None:
            self.head= new_node
        else:
            current = self.head
            while current.nxt:
                current = current.nxt
            current.nxt = new_node

        self.size+=1
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        current = self.head
        index=0

        while current:
            if index==(self.size//2):
                print(index)
                return
            current=current.nxt
            index+=1
        print(-1)
        return

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 
