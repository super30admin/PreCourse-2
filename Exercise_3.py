# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):
        self.data= data
        self.next= None  
        
class LinkedList: 
  
    def __init__(self): 
        self.head = None
  
    def push(self, new_data): 
        newNode = Node(new_data)
        newNode.next= self.head
        self.head= newNode

        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        if (self.head == None):
            return
        len_node = self.head
        len=0
        while (len_node is not None):
            len_node= len_node.next
            len = len + 1
        # print("total length", len)
        mid= len//2
        # print("mid", mid)
        mid_node = self.head
        # print('head',self.head.data)
        while ( mid):
            mid_node = mid_node.next
            mid = mid - 1
        print(mid_node.data)
        return mid_node.data

            


# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 
