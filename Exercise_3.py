# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):  
        self.data = data
        self.next = None

class LinkedList: 
  
    def __init__(self): 
        self.head = None
        self.count = 0
  
    def push(self, new_data): 
        if (self.head == None):
            self.head = Node(new_data)
        else:
            newNode = Node(new_data)
            newNode.next = self.head
            self.head = newNode
  
        self.count +=1
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        if self.count == 1:
            return self.head

        else:
            mid = self.count // 2
            secondCount = 0
            while self.head:
                if mid == secondCount:
                    return self.head
                self.head = self.head.next
                secondCount+=1

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
res = list1.printMiddle() 
print(res)
