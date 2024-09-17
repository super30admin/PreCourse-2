import math
# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList: 
  
    def __init__(self):
        self.head = None
    
    def print(self):
        temp = self.head
        if self.head != None:
            while temp != None:
                print(temp.data)
                temp = temp.next
        else:
            print("Linked List is Empty")
        print("==================")
  
    def push(self, new_data): 
        if self.head == None:
            self.head = Node(new_data)
        else:
            temp = self.head
            while temp.next!=None:
                temp = temp.next
            newnode = Node(new_data)
            temp.next = newnode
            
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        count = 0
        curr = self.head
        while curr != None:
            count = count+1
            curr = curr.next
        half = math.ceil(count/2)
        temp = self.head
        for i in range(0,half-1):
            temp = temp.next
        print(temp.data)            

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.print()
list1.push(4)
list1.print()
list1.push(2)
list1.print()
list1.push(3)
list1.print()
list1.push(1) 
list1.print()
list1.printMiddle() 