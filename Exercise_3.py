'''
====== Submission Details =======
Student Name: Pavan Kumar K. N.
Email       : pavan1011@gmail.com
S30 SlackID : RN32MAY2021
=================================
'''

# Node class  
class Node:  
    # Function to initialise the node object  
    # Renamed "next" to next_node since next is a keyword - 
    def __init__(self, data, next_node = None):

        # Data module of the linked list node 
        self.data = data 
        # Pointer to next_node node in the linked list
        self.next_node = next_node 

    #Prints the node and the following linked list
    def __str__(self):
        str_repr = ""
        str_repr = f"{self.data}->"

        #Recursive call
        if self.next_node is not None:
            str_repr += self.next_node.__str__()
        else:
            str_repr += "NULL"

        return str_repr
        
class LinkedList: 

    def __init__(self): 
        self.head = None
        
    # Function to push new data as a node at the head of the linked list
    def push(self, new_data):
        
        # print(f"Pushing data: {new_data}")
        
        # Create a new node with next = NULL
        new_node = Node(new_data)

        # print(f"    Created new node: {new_node}")
        
        # Link the new node's "next_node" pointer to previous head
        new_node.next_node = self.head
        
        # print(f"    new node: {new_node}")

        # Update head to point to new node
        self.head = new_node
        
        # print(f"    Pushed node. Head is now:{self.head}")

    
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        # Initialization

        # last is a pointer that will traverse  the linked list
        last = self.head

        # mid is a pointer that to the mid element of the linked 
        # list traversed so far
        mid = self.head

        # Count is used to increment mid every other iteration of the traversal
        # last will move through the list twice as fast as 
        count = 0

        #Traverse linked list
        while last is not None:
            if count&1 == 1:
                # Increment mid to point to next node if count is odd
                # effectively traversing the list at half the rate of last
                mid = mid.next_node
            # Increment last to next node every iteration
            last = last.next_node
            count+=1

        print(f"Middle data: {mid.data}\nMiddle node: {mid}")

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1)
print(f"Input: {list1.head}")

list1.printMiddle() 
