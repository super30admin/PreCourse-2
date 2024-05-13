# Node class  
#time complexity O(N)
#Space complexity O(1)
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):  
        self.data=data
        self.next=None
        
class LinkedList: 
  
    def __init__(self): 
        self.head=None
        
  
    def push(self, new_data): 
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node
            
        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        '''
        We initialize both p1 and p2 to the head.We use p1 to move two steps and p2 to move one step .
        when p1 reaches the end of the list  p2 will be at the middle node of the linked list.
        '''
        #intializing to head
        p1 = self.head 
        p2 = self.head

        if self.head is not None:
            while p1 is not None and p1.next is not None:
                p1 = p1.next.next #traversing 2 steps
                p2 = p2.next
            print("The middle element is:", p2.data)

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 

#error encounter at adding new node i added new_data instead of new_node 
#already did on leetcode

