#Time Complexity: to just find position O(1) by maintaining size of list, to find element O(n)
# Node class  

class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):  
        self.data = data
        self.next = None
        
class LinkedList: 
  
    def __init__(self): 
        self.head = None
        self.size = 0
  
    def push(self, new_data): 
        newNode = Node(new_data)
        n = self.head
        if self.head == None:
            self.head = newNode
            self.size+=1
        else:
            while n.next is not  None:
                n = n.next
            n.next = newNode
            self.size+=1
        


  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        self.index = 0
        n = self.head
        if n is not None:
            while self.index<self.size//2:
                n = n.next
                self.index+=1
            print(n.data)
        else:
            print('No elements in the list')

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 
