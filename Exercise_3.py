# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data=0,next=None):  
        self.data = data
        self.next = next
        
class LinkedList: 
  
    def __init__(self): 
        # Initialise the head node
        self.head = Node()
  
    def push(self, new_data): 
        # Append a new node to the list if we have a head node or assign the new node as head node
        if self.head is None:
            newNode = Node(new_data)
            self.head = newNode
            return
        newNode = Node(new_data)
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = newNode
        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        # use 2 pointers slow and fast to fetch the middle node.
        slow,fast = self.head,self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        print("Value of Middle Node: ",slow.data)

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.push(10)
list1.push(11)
list1.printMiddle() 
