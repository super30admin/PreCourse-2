# time complexity = O(n)
# space complexity= O(n) 
# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data=None):  
        self.data=data
        self.next=None
        
class LinkedList: 
  
    def __init__(self): 
        self.head=Node()
        self.count=0
  
    def push(self, new_data): 
        newNode=Node(new_data)
        self.count+=1
        if self.count==0:
            self.head.next=newNode
        else:
            temp=self.head
            while temp.next!=None:
                temp=temp.next
            temp.next=newNode

        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        mid=int(self.count/2) 
        temp=self.head.next
        for i in range(0,mid):
            temp=temp.next
        print(f"middle value is {temp.data} ") 
    
    def print(self):
        temp=self.head.next
        while temp!=None:
            print(temp.data)
            temp=temp.next



# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 
