#Time complexity = O(n)
#Space complexity = O(1)

# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):  
        self.data=data
        self.next=None
        
class LinkedList: 
  
    def __init__(self): 
        self.head=None
  
    def push(self, new_data): 
        if(self.head==None):
            self.head=Node(new_data)
        else:
            node=self.head
            while(node.next!=None): #adding values at the end of the list
                node=node.next
            node.next=Node(new_data)
            
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        node1=self.head
        node2=self.head
        while(node2.next!=None and node2.next.next!=None): # when node2 reaches the end , node1 reaches the midpoint as node2 traverses 2 steps at a time
            node1=node1.next
            node2=node2.next.next       
        print(node1.data)
# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 
