# Python program to Find Mid Point of a Singly Linked List.

# Time Complexity : O(n)
# Space Complexity : O(1)
# Did this code successfully run on VScode : Yes
# Any problem you faced while coding this : No

# Node class  
class Node:  
  
    # Function to initialise the node object  

    # Created an empty node
    def __init__(self, data):           
        self.data = data
        self.node = None
        
class LinkedList: 
    
    # head initiated
    def __init__(self):                 
        self.head = None
        
    # function to push data into the nodes    
    def push(self, new_data):           

        # pushed new data into node using Node function
        new_node = Node(new_data)    

        # Only one node yet so pointing the next pointer to head
        new_node.next = self.head

        # pointing the head to the only node
        self.head = new_node             

    # Function to get the middle of  
    # the linked list 

    # Using 2 pointer approach. Incrementing slow pointer by 1 and fast pointer by 2
    # If end of list is reached by fast pointer, slow pointer will point to mid
    def printMiddle(self):
        slow = self.head                
        fast = self.head                

        # as long as logical value of (fast and fast.next) is true, elements still present in list
        while fast and fast.next:  

            # incrementing slow pointer by 1, fast pointer by 2     
            slow = slow.next            

            # if this loop ends, end of list has been reached
            fast = fast.next.next       

        print("Middle of the list is ", slow.data)

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 
