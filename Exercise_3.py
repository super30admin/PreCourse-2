# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data,link): 
        self.val = data
        self.link = link 
        
class LinkedList: 
  
    def __init__(self,head= None): 
        self.head = head
        
  
    def push(self, new_data): 
        newNode = Node(new_data,self.head)
        self.head = newNode
        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        result = []
        while self.head:
            result.append(self.head.val)
            self.head = self.head.link
        print(result[len(result)//2])

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 
