# Time Complexity :or o(n)
# Space Complexity :O(n)
# Did this code successfully run on Leetcode :
# Any problem you faced while coding this :no
# Python program for implementation of Quicksort Sort 
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
        new=Node(new_data)
        new.next=self.head
        self.head=new
        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        first=self.head
        last=self.head
        while last and last.next:
            first=first.next
            last=last.next.next
        print(first.data)
        
       
        
            


# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 
