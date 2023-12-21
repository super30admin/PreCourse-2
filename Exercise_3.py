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
        currentNode = Node(new_data)
        if self.head == None:
            self.head = currentNode
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = currentNode
            self.count += 1
        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        mid = self.count // 2
        currentNode = self.head
        index = 0
        if currentNode == None:
            return -1
        while index != mid:
            currentNode = currentNode.next
            index += 1
        print(currentNode.data)

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1)
list1.printMiddle() 
