# Time Complexity : O(n) because the printMiddle method dominates the time complexity due to its linear traversal of the linked list.
# Space Complexity: O(1) because it uses a constant amount of additional space that does not depend on the size of the linked list.
#  Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):  
        self.data = data
        self.next = None
        
class LinkedList: 
  
    def __init__(self): 
        self.head = None
        
  
    def push(self, new_data): 
        newnode = Node(new_data)
        newnode.next = self.head
        self.head = newnode
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        slowptr = self.head #Initialize slow pointer
        fastptr = self.head #Initialize fast pointer

        while fastptr is not None and fastptr.next is not None: #Check if the fast pointer and next element after fast pointer is not None
            slowptr = slowptr.next #Move slow pointer to the next element
            fastptr = fastptr.next.next #Move fast pointer to next to next element. 

        #When the fast pointer reached the last element, the slow pointer would be the middle element
        #Print the middle element that is the slow pointer data
        print("The middle element is:", slowptr.data)

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 
