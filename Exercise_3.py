# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data=None,next=None):
        self.data = data
        self.next = next  
        
class LinkedList: 
  
    def __init__(self):
        self.head = None
        self.numberOfNodes = 0 
        
  # Declared Number of Nodes as a track 
  # But we can also iterate over the linked list find the lenght and then do accordingly
  # assuming we are free to use either tracking is better as we do not have to go throught the list everytime we need it (length)
    def push(self, new_data): 
        self.numberOfNodes += 1
        node = Node(new_data)

        if self.head == None:
            self.head = node
        else:
            curr = self.head
            while curr.next != None:
                curr = curr.next
            curr.next = node



        
       
        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        if self.numberOfNodes%2 !=0:
            curr = self.head
            for i in range(0,self.numberOfNodes//2):
                curr = curr.next
            print(curr.data)
        else:
            curr = self.head
            prev = None
            for i in range(0,(self.numberOfNodes//2)):
                prev = curr
                curr = curr.next
            print("Two middles",prev.data,curr.data)





# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 
