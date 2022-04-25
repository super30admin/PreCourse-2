# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self,data,next=None):
        self.data = data
        self.next = None  
        
class LinkedList: 
  
    def __init__(self): 
        self.head = None
  
    def push(self, new_data):
        if self.head == None:
            node = Node(new_data)
            self.head = node
        else:
            node = Node(new_data)
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = node
     
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        curr = self.head
        count = 0
        while curr:
            curr = curr.next
            count += 1
        mid = count//2
        curr = self.head
        count = 0
        while curr:
            if count == mid:
                return curr.data
            else:
                curr = curr.next
                count += 1

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
print(list1.printMiddle()) 
