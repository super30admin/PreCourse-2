# PreCourse_2: Exercise_3: Find Mid Point of a Singly Linked List

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
        newNode.next = self.head
        self.head = newNode
        
    # Function to get the middle element of the linked list 
    def printMiddle(self): 
        slowPointer = self.head
        fastPointer = self.head

        if self.head != None:
            while (fastPointer != None and fastPointer.next != None):
                slowPointer = slowPointer.next
                fastPointer = fastPointer.next.next
            print ("The middle element of the LinkedList is ", slowPointer.data)

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 
