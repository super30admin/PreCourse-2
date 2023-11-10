# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):  
        self.data = data
        self.next = None

        
class LinkedList: 
  
    def __init__(self): 
        self.head = None
        
  
    def push(self, new_data): 
        newNode = Node(new_data)
        newNode.next = self.head
        self.head = newNode
        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        slowPtr = self.head
        fastPtr = self.head
        #till fastPtr reach the end
        while fastPtr and fastPtr.next:
            slowPtr = slowPtr.next
            fastPtr = fastPtr.next.next
        print(slowPtr.data)


# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 

#5,4,3,1 -> middle should be 3