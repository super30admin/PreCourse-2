# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):  
        self.data=data
        self.next=None
        
class LinkedList: 
  
    def __init__(self): 
        self.head=None
        self.link=0

        
  
    def push(self, new_data): 
        t=Node(new_data)
        if(not self.head):
            self.link+=1
            self.head=temp
        else:
            self.link+=1
            a=self.head
            while(a.next):
                a=a.next
            a.next=t
        return self.head
        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        mid=(self.link)//2+1
        x=self.head
        while (mid>1):
            mid-=1
            x=x.next
        return x.data

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 
