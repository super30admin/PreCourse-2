# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):  
        self.data = data
        self.next = None

class LinkedList: 
  
    def __init__(self): 
        self.head = None
        self.counter = 0
  
    def push(self, new_data): 
        if self.head == None:
            self.head = Node(new_data)
        else:
            node = self.head
            while node.next:
                node = node.next
                
            node.next = Node(new_data)
        self.counter += 1
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        node = self.head
        for num in range((self.counter // 2) - 1):
            node = node.next 
        print(node.next.data)   


# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle()
