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
        curr = self.head 
        if curr is None:
            self.head = Node(new_data)
            print(f'head data {self.head.data}')
        else:
            while curr is not None and curr.next is not None:
                curr = curr.next
            curr.next = Node(new_data)
        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        curr = self.head
        length = 0
        while curr is not None:
            length = length + 1
            curr = curr.next

        mid = length//2
        curr = self.head

        for _ in range (mid):
            curr = curr.next
        return curr.data



        


# Driver code 
list1 = LinkedList() 
list1.push(5)
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
print(list1.printMiddle()) 
