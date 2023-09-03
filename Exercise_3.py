# Time Complexity : O(N)
# Space Complexity : O(1)
# Did this code successfully run on Leetcode :

# Any problem you faced while coding this :

# Your code here along with comments explaining your approach
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):  
        self.data= data
        self.next=None
        
class LinkedList: 
  
    def __init__(self): 
        self.head=Node(None)
        self.first_node=True
        self.curr=self.head
        self.size=0
  
    def push(self, new_data): 
        if(self.first_node):
            self.head.data=new_data
            self.size+=1
            self.first_node=False
        else:
            new_node= Node(new_data)
            self.curr.next=new_node
            self.curr=self.curr.next
            self.size+=1
  
    # Function to get the middle of  
    # the linked list 
    def print_list(self):
        t= self.head
        while(t!=None):
            print(t.data)
            t=t.next
    def printMiddle(self): 
        t=self.head
        for i in range(self.size//2):
            t=t.next
        print(t.data, "lies in the middle")

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 
# list1.print_list()
