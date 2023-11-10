# Node class  
from platform import node


class Node:  
    # Function to initialise the node object  
    def __init__(self, data=None, next=None):  
        self.data = data #Data will hold the value of the element
        self.next = next #Next will have the link to the next node
        
class LinkedList: 
  
    def __init__(self):
        self.head = None #Initialize head
        
    # Time Complexity : O(n)
    # Space Complexity : O(1)
    def push(self, new_data): 
        new_node = Node(new_data) #Instantiate the Node object
        if(self.head == None):
            self.head = new_node #Instantiated node will be the head if the linked list is empty
        else:
            current = self.head #Declare and define current variable to loop through the end of the linked list
            while(current.next):
                current = current.next #Loop through the list one by one until the end is reached
            current.next = new_node #Link the new node to the end of the linked list

    # Function to get the middle of  
    # the linked list
    # Time Complexity : O(n)
    # Space Complexity : O(1)
    def printMiddle(self): 
        if self.head != None: #Empty list check
            temp = self.head #temp will be used to loop through the list and calculate the length. We start with the head
            len = 0 #Initialize len variable to 0. It will be used to calculate the length

            while(temp != None): #While we have not reached the end of the node
                len += 1 #Increment len variable
                temp = temp.next #Iterate to the next node

            temp = self.head #Re-initialize temp to head. It will be used to get the mid node
            mid = len // 2 #Divide the calculated length by 2 to get the middle number

            while mid != 0: #Iterate mid number of times in decreasing order of mid
                temp = temp.next #Keep progressing to the next nodes starting from head
                mid -= 1 #Decrement mid
            
            print("Middle Element: ", temp.data)
        

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 
