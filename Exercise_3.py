# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data): 
        self.val=data
        self.next=None
        
class LinkedList: 
  
    def __init__(self): 
        self.head=None
        self.counter=0

    def push(self, new_data): 
        if self.head==None:
            self.head=Node(new_data)
            self.counter+=1
        else:
            temp = self.head
            while(temp.next!=None):
                temp=temp.next
            temp.next= Node(new_data)
            self.counter+=1
        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        if self.head ==None:
            print("No elements in linked list")
        else:
            temp=self.head
            count = self.counter//2
            while(temp!=None):
                if count==0:
                    print("Middle element is:", temp.val)
                count-=1
                temp=temp.next

         
# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 
