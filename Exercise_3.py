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
        if self.head is None:
            self.head = newNode
        else:
            newHead = self.head
            while newHead.next is not None:
                newHead = newHead.next
            newHead.next = newNode
        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        # count length:
        lengthList = 0
        newHead = self.head
        while newHead is not None:
            lengthList += 1
            newHead = newHead.next
        mid = lengthList // 2

        i = 0
        newHead = self.head

        #run loop through midpoint and print element
        while i < mid:
            newHead = newHead.next
            i += 1
        print(newHead.data)


# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2)
list1.push(3) 
list1.push(1) 
list1.printMiddle() 
