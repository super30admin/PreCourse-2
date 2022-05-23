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
        newnode=Node(new_data)       
        curr=self.head   
        if self.head==None:
            self.head=newnode
            return
        else:
            newnode.next=self.head
            self.head=newnode
            print(" Newly added and last itme ",self.head.data)
            return
            
        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        print(self.head.data)
        curr=self.head
        count=0
        while curr!=None:
            count+=1
            curr=curr.next
        print("count=", count)
        midnode_indx=count//2
        print("midnode_indx =",midnode_indx) 
        ptr=self.head
        mid_counter=0
        while mid_counter!=midnode_indx:
            mid_counter+=1
            ptr=ptr.next
        print("@@@", ptr.data)
        return ptr.data
            

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 
