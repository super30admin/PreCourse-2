# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):
        self.data = data
        self.next = None  
        
class LinkedList: 
  
    def __init__(self): 
        self.head=None
        
  
    def push(self, new_data): 
        temp = Node(new_data)
        temp2=self.head
        if not temp2:
            self.head = temp
            return
        while temp2.next !=None:
            temp2 = temp2.next
        temp2.next = temp
        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        if not self.head:
            return None
        elif not self.head.next:
            return self.head
        else:
            temp1=self.head
            temp2 = self.head.next
            while temp2.next != None and temp2.next.next !=None:
                temp2 = temp2.next.next
                temp1=temp1.next
            return temp1



# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
a= list1.printMiddle() 
print(a.data)
