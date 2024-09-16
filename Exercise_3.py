# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):  
        self.data = data
        self.next = None
        
class LinkedList: 
  
    def __init__(self): 
        self.head = None
        
  
    def push(self, new_data): #adding element to the end of the linked list
        n = Node(new_data)
        if self.head is None:
            self.head = n
            return
        
        temp = self.head
        while(temp.next):
            temp=temp.next
        temp.next = n
        

        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        if self.head is None:
            return None
        
        temp = self.head
        c = 0
        while(temp):
            temp = temp.next
            c+=1
        m = c//2

        temp = self.head
        for i in range(0,m):
            temp=temp.next
        print (temp.data)




# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 
