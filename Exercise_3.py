#Time Complexity: for Push, for finding middle O(N) 
#Space Complexity: O(N)
# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data,next):
        self.data= data  
        self.next= next
        
class LinkedList: 
  
    def __init__(self): 
        self.head = None 
        self.next= None     
        
  
    def push(self, new_data): 
        new= Node(new_data,None)
        #Inserting at head
        if not self.head: 
            self.head = new
        else:
            curr= self.head
            while curr.next:
                curr = curr.next
            curr.next = new

        
    #Two pointers Slow and Fast
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        s = self.head
        f = self.head
        while f and f.next:
            s= s.next
            f = f.next.next
        return s.data

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.push(9) 
list1.push(8) 
list1.push(6) 
list1.push(7) 
list1.push(11) 
list1.push(12)

print(list1.printMiddle())
