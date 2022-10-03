# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):
        self.data = data
        self.next = None  
        
class LinkedList: 
    def __init__(self): 
        self.head = None
        self.length = 0
  
    def push(self, new_data): 
        node = Node(new_data)
        self.length +=1

        if self.head == None:
            self.head = node
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = node
        node.next = None
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        if self.head == None:
            return 
        curr = self.head
        count = 0
        mid = (0 + self.length)//2
        print(mid)
        while curr and (count != (self.length//2)) :
            curr = curr.next
            count +=1

        return curr.data
# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 
