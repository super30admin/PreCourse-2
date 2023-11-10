# Node class  
import math
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList: 
  
    def __init__(self): 
        self.head=None
        self.counter=0


    def push(self, new_data):
        self.counter=self.counter+1
        if self.head==None:
            self.head=Node(new_data)
        else:
            current=self.head
            while current.next is not None:
                current=current.next
            new_node=Node(new_data)
            current.next=new_node
            new_node.next=None

    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        mid=math.ceil(self.counter/2)
        scan=self.head
        for i in range(mid-1):
            scan=scan.next
        if self.counter%2==0:
            print(scan.data, scan.next.data)
        else:
            print(scan.data)



# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1)
list1.push(309) 
list1.push(123)
list1.printMiddle() 
