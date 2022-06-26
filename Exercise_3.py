# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):  
        self.data = data
        self.next = None
        
class LinkedList: 
  
    def __init__(self): 
        self.head = None
        self.length = 0
        
  
    def push(self, new_data): 
        new_node = Node(new_data)
        if(self.head == None):
            self.head = new_node
        else:
            temp = self.head
            while(temp.next!=None):
                temp = temp.next
            temp.next = new_node
        self.length+=1

        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        if(self.length == 0):
            print("No nodes are present in the linked list")
        elif(self.length == 1):
            print(self.head.data)
        else:
            mid = int(self.length/2)
            temp = self.head
            for i in range(0,mid-1):
                temp = temp.next
            if((self.length/2)>mid):
                print(temp.next.data)
            else:
                print(temp.data)
            

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle()
