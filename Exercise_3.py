# Node class  
class Node:  
    # Function to initialise the node object  
    def __init__(self, data):  
        self.data = data
        self.next = None
        
class LinkedList: 
  
    def __init__(self): 
        self.head = None 
        self.rear = None #Push Operation is optimised to O(1)
        
  
    def push(self, new_data):
        newNode = Node(new_data)

        if self.head == None: #If list is empty.
            self.head = newNode
            self.rear = self.head
            return

        self.rear.next = newNode #If list already has an element.
        self.rear = self.rear.next
        
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        slow = self.head
        fast = self.head
        #Using two pointers. Slow pointer moves one step at a time.
        #Fast pointer moves two steps at a time.
        while fast.next != None and fast.next.next != None:
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
