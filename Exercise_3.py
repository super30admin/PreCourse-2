# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data=None):  
        self.data = data
        self.next = None

class LinkedList: 
  
    def __init__(self): 
        self.head = Node()
        self.last = self.head
  
    def push(self, new_data): 
        if self.head.data == None:
            self.head.data = new_data
            return
        
        new_node = Node(new_data)
        n = self.head
        while (n.next != None):
            n = n.next
        n.next = new_node
        self.last = new_node
    
    def displayList(self):
        n = self.head
      #  print(self.head.data,self.head.next)
        while (n != None):
            print(n.data,end = " ")
            n = n.next
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        print()
        if (self.head.data == None):
            print("list is empty")
            
        #Find the length of the linked list
        lenth = 1
        temp = self.head
        while(temp.next != None):
            lenth+=1
            temp = temp.next
        #print(lenth)
        
        #if even, e.g. 6, take 3rd element.
        mid = int((lenth+1)/2)
        #print(mid)
        
        temp = self.head
        for i in range(mid-1):
            temp = temp.next
            
        print(temp.data)

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 

list1.displayList()

list1.printMiddle() 
