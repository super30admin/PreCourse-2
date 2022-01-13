# Node class  
#time complexity: O(n)
#Space complexity: O(1)
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):  
        self.data= data 
        self.next = None
        
class LinkedList: 
  
    def __init__(self): 
        self.head = Node(None)
        self.count= 0  # counts no of linkeds list in data 
  
    def push(self, new_data): 
        if self.data.head== None:
            self.headh.data= new_data
        else:
            newNode= Node(new_data)
            curr =self.head  
            while(curr.next != None):
                 curr =curr.next 
            curr.next=newNode
        self.count +=1 
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        curr = self.head
        for _ in range(self.count//2):
            curr= curr.next
        print(curr.data)

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 
