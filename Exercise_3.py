# Node class  
# Time Complexity : O(n)
# Space Complexity : O(1)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):  
        self.data=data
        self.next=None
        
class LinkedList: 
  
    def __init__(self): 
        self.head=None
        
  
    def push(self, new_data): 
        node=Node(new_data)
        node.next=self.head
        self.head=node
        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        #let us consider the head of the linked list as the midpoint
        mid=self.head
        
        count=0
        pointer=self.head
        
        if self.head is None:
            print("Linked List is empty")
        else:
            while pointer is not None:
                #Check if the counter is odd, if yes then update the midpoint as the next node
                if(count%2)!=0:
                    mid=mid.next
                count+=1
               
                pointer=pointer.next
        
            print("Middle element is: ", mid.data)

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1)

list1.printMiddle() 
