# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data): 
        self.data = data
        self.next = None
        
class LinkedList: 
  
    def __init__(self): 
        self.head = None
        self.lenCount = 0
  
    def push(self, new_data): 
        n_node = Node(new_data)
        self.lenCount += 1
        if self.head == None:
            self.head = n_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = n_node
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        mid = self.lenCount//2
        curr = self.head
        while mid:
            curr = curr.next
            mid -= 1
        print(curr.data)
            



# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 
