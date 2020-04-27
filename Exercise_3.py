#Time Complexity = O(N)
#Space Complexity = O(N)

# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data): 
        self.Data = data
        self.next = None
        
class LinkedList: 
  
    def __init__(self): 
        self.counter = 0
        self.head = None
        
  
    def push(self, new_data): 
        newnode = Node(new_data)
        if self.head == None:
            self.head = newnode
            self.counter+=1
        else:
            curr = self.head
            while(curr.next!=None):
                curr = curr.next
            curr.next = newnode
            self.counter+=1
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        curr = self.head
        i = 1
        while i <= self.counter//2:
            curr = curr.next
            i = i+1
        return curr.Data
            

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1)
a = list1.printMiddle() 
print(a)
