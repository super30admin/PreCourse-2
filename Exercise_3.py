# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):
        self.data = data
        self.next = None

        
class LinkedList: 
  
    def __init__(self):
        self.head = None
        self.prev = None
        self.length = 0
  
    def push(self, new_data):
        newNode = Node(new_data)
        if self.head == None:
            self.head = newNode
            self.prev = self.head
            self.length += 1
        else:
            self.prev.next = newNode
            self.prev = newNode
            self.length += 1
        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        mid = (self.length-1)//2

        if mid <= 0:
            print(self.head)
            return

        tempHead = self.head

        while mid>0:
            tempHead = tempHead.next
            mid -= 1

        print(tempHead)

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 
