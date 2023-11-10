# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):

        self.data = data
        self.next = None
        
class LinkedList: 
  
    def __init__(self):
        
        self.node = None
        self.head = None
        self.count = 0
        self.hash = {}        
  
    def push(self, data):

        if(self.head == None):

            temp = Node(data)
            self.head = temp
            self.node = temp
            self.hash[self.count] = self.node
            self.count = self.count + 1

        else:

            temp = Node(data)
            self.node.next = temp
            self.node = temp
            self.hash[self.count] = self.node
            self.count = self.count + 1
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):

        if(self.count == 0):
            
            return None

        elif(self.count < 2):

            i = self.head

            print('Mid point data is: ', i.data)
            print('Mid point address is: ', i.next)

        mid = (self.count - 1)/2

        print('Address: ',self.hash[mid])        
        print('Data: ',self.hash[mid].data)


        

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 
