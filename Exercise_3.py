""""Python implementation for returning the middle element of a LinkedList"""

""" Time Complexity O(n) since we are traversing through the list once using fast n slow pointers

Program did not give correct results for even no. of elements in the list"""

# Node class  
class Node:  
  
    # Constructor to initialise the node object  
    def __init__(self, data):
        self.data = data
        self.next = None #assign a new node pointing to NULL
        
class LinkedList: 
  
    def __init__(self): 
        self.head = None #initialise head node to NULL
        
  
    def push(self, new_data):
        new_node = Node(new_data) #Assign the new node with the given data
        new_node.next = self.head #Assign head pointer to new node
        self.head = new_node      #Assign new node to head node
                
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        slow = self.head #fast pointer starts from head node
        fast = self.head #slow pointer starts from head node
        if self.head is not None: #check for empty list
            while (fast.next is not None and fast is not None): #Check for fast pointer going overboard
                fast = fast.next.next #jump fast pointer two steps ahead
                slow = slow.next #assign slow pointer one step ahead
            print("The element at the middle is :",slow.data) #print middle element

    
#Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1)
list1.printMiddle() 