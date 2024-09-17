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
        new_data = Node(new_data)
        new_data.next = self.head
        self.head = new_data 
        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        if self.head is None:
            print("linked list is empty! ")
            return

        count = 0
        n = self.head
        while n is not None:
            n = n.next
            count = count + 1

        middle_index = count // 2

        n = self.head
        for i in range(middle_index):
            n = n.next

        print("the middle element is",n.data)
        


# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 
