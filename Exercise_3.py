#TimeComplexity:
    #push: O(n)
    #printMiddle: O(n)
#SpaceComplexity: O(n)

# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):  
        self.data = data
        self.next = None
        
class LinkedList: 
  
    def __init__(self): 
        #maintain the length of LL and a pointer to start of LL
        self.list_len = 0
        self.head = None
  
    def push(self, new_data): 
        
        #create a new node
        n = Node(new_data)
        
        #if LL is empty point the head to it
        if self.list_len == 0:
            self.head = n
        #if LL is not empty, point the last node in LL to the new node
        else:
            tail = self.head
            while tail.next != None:
                tail = tail.next
            tail.next = n
        
        #increase the length of the LL by 1
        self.list_len += 1
            
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        
        #find the middle element by half of length
        mid = self.list_len // 2
        #start from head to find the middle element
        pointer = self.head
        for i in range(mid):
           pointer = pointer.next
        
        print(pointer.data)  

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 
