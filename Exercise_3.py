# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):
        self.data = data
        self.link = None

        
class LinkedList: 
  
    def __init__(self):
        self.head =None

    def push(self, new_data):
        newNode = Node(new_data)
        newNode.link = self.head
        self.head = newNode
        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        slow,fast = self.head,self.head
        while fast!=None and fast.link!=None:
            slow = slow.link
            fast = fast.link.link
        print("Middel node is",slow.data)


# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 
