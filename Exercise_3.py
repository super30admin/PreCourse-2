# Time Complexity - O(n)
# Space Complexity - O(1)

# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):  
        self.data = data
        self.next= None
        
class LinkedList: 
    def __init__(self):
        self.head = None   
  
    def push(self, new_data): 
        new_node = Node(new_data)
        if self.head is None: 
            self.head = new_node
        curr = self.head 
        while curr.next: 
            curr = curr.next
        curr.next =  new_node 

    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        lptr=self.head
        rptr=self.head

        if self.head is not None:
            while(rptr is not None and rptr.next is not None):
                rptr=rptr.next.next
                lptr=lptr.next
            print("The middle element is: ",lptr)
        
        

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle()
