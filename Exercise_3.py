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
        newnode = Node(new_data)
        newnode.next = self.head
        self.head = newnode
        return
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        i = self.head
        j = self.head

        while i and i.next:
            i = i.next.next
            j = j.next
        print("Middle element:" ,j.data)
        return

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 
