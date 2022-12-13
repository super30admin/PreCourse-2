# Time Complexity : 0(n)
# Space Complexity :O(n)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this :No


# Node class  
class Node:  
  # Function to initialise the node object  
    def __init__(self, data): 
        self.data=data
        self.next=None 
        
class LinkedList: 
  
    def __init__(self): 
        self.head=Node(None)
        
  
    def push(self, new_data): 
        if(self.head.data==None):
            self.head.data=new_data
        else:
            new_node=Node(new_data)
            iterr=self.head
            while(iterr.next!=None):
                iterr=iterr.next
            iterr.next=new_node


    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        p1=self.head
        p2=self.head
        while(p2!=None and p2.next!=None):
            p1=p1.next
            p2=p2.next.next
        print(p1.data)



# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 
