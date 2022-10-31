'''
Time Complexity
O(n/2) since the loop runs only n/2 times 

Space complexity 
O(n) since n number of nodes needs to be created

Aprroach
have a count of number of elements
mid = count/2
loop the list from head to mid

'''
#  Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):
        self.data  = data
        self.next = None  
        
class LinkedList: 
  
    def __init__(self):
        self.c = 0 #To have a count easy to find middle element 
        self.head = None
        self.prev = None
        
  
    def push(self, new_data):
        newNode = Node(new_data)
        if self.head == None:
            
            self.head = newNode
            self.prev = newNode
            self.c+=1
        else:
            self.prev.next = newNode
            self.prev = newNode
            self.c+=1
            

        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        curr = self.head
        if curr==None:
            print("No elements")
        else:
            i = 0
            mid = (self.c//2)
            while i<mid:
                curr = curr.next
                i+=1
        return curr.data

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
print(list1.printMiddle()) 