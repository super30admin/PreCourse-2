# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):
        self.data = data
        self.next = None
        self.middle = None
        
class LinkedList: 
  
    def __init__(self): 
        self.head = Node(None)
        self.current = None
        self.middle = None        
  
    def push(self, new_data):
        if self.head.data == None:
            self.head.data = new_data
            return
        
        self.current = self.head
        while self.current.next != None:
            self.current = self.current.next

        self.current.next = Node(new_data)
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        self.current = self.head
        self.middle = self.head
        while self.current.next != None:
            self.current = self.current.next
            self.middle = self.middle.next
            if self.current.next != None:
                self.current = self.current.next
            else:
                print(self.middle.data)
                return 
        print(self.middle.data)
        return 


# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 
