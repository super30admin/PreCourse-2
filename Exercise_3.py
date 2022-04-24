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
        '''
        time complexity: O(1)
        space complexity: O(n)
        '''
        if(self.head==None):
            self.head = Node(new_data)
        else:
            new_node = Node(new_data)
            new_node.next = self.head
            self.head =  new_node
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        '''
        time complexity: O(n/2)
        space complexity: O(1)
        '''
         
        ptr1 = self.head
        ptr2 = self.head.next

        while(ptr2 and ptr2.next):
            ptr1 = ptr1.next
            ptr2 = ptr2.next.next
        print(ptr1.data)

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 
