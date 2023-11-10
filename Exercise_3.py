# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):  
        self.data = data
        self.next = None
        
class LinkedList: 
  
    def __init__(self): 
        self.head = None
        self.i = 0
        
  
    def push(self, new_data): 
        temp = Node(new_data)
        if(not self.head):
            self.i += 1
            self.head = temp
        else:
            self.i += 1
            t = self.head
            while(t.next):
                t = t.next
            t.next = temp
        return self.head
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        j = (self.i) // 2 + 1
        k = self.head
        while(j > 1):
            j -= 1
            k = k.next
        return k.data
        

# Driver code 
list1 = LinkedList() 
list1.push(5)
list1.push(4) 
list1.push(2) 
list1.push(3) 
# list1.push(1)
print(list1.printMiddle())
