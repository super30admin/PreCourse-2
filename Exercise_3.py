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
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        temp = self.head
        count = 0

        while self.head:
            if (count & 1):
                temp = temp.next
            self.head = self.head.next

            count += 1

        print(temp.data)

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2)
list1.push(3) 
list1.push(1) 
list1.printMiddle() 
