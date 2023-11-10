# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):
        self.data = data
        self.next = None  
        
class LinkedList: 
    def __init__(self): 
        self.start = None
        
  
    def push(self, data): 
        node = Node(data)
        if self.start == None:
            self.start = node
        else:
            var = self.start
            while var.next != None:
                var = var.next
            var.next=node
        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        var = self.start
        f1=1
        while var.next != None:
            var = var.next
            f1+=1
        var = self.start
        f2=1
        while var.next != None:
            if f2==(f1//2)+1:
                print(var.data)
                break
            var = var.next
            f2+=1

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 
