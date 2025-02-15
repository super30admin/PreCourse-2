# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):  
        # initialize the data and next pointer of the nodes
        self.data = data
        self.next = None
        
class LinkedList: 
  
    def __init__(self): 
        # initialze the linked list with None
        self.head = None  
  
    def push(self, new_data): 
        # create a node for the new_data
        newNode = Node(new_data)
        # set the next pointer of new node to head
        newNode.next = self.head
        # set head to newNode which is the head of the linked list
        self.head = newNode
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        # initialze the slow and faster pointer to head of linked list
        slow = self.head
        fast = self.head
        # loop till fast and fast.next is not None
        while fast and fast.next:
            # move slow by 1 position
            slow = slow.next
            # move fast by 2 position
            fast = fast.next.next
        # in this way when fast pointer reach to end of the list that time slow pointer will reach to middle of the linked list
        print(slow.data)

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 
