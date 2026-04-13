# Node class  
class Node:
    # Function to initialise the node object  
    def __init__(self, data,next=None):
        self.data = data
        self.next = next
        
class LinkedList: 
  
    def __init__(self): 
        self.head = Node(-1)
  
    def push(self, new_data):
        temp = self.head
        while temp.next:
            temp = temp.next
        newNode = Node(new_data)
        temp.next = newNode
        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        slow,fast = self.head.next,self.head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        print(slow.data)

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 
