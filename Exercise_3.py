# Node class  
#Time complexity:O(n)
#space complexity: O(1)
#Ran in leetcode: yes
#problems/issues: None
# use 2 pointers. The faster pointer moves twice for every one movement of slowest pointer. When faster pointer cannot proceed further,
# the slow pointer will point to the middle element.
from requests import head


class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):
        self.data=data
        self.next=None  
        
class LinkedList: 
  
    def __init__(self):
        self.head=None
        self.N=0 
        
  
    def push(self, new_data):
        node=Node(new_data)
        self.N+=1
        if(self.head==None):
            self.head=node
        else:
            temp=self.head
            while(temp.next):
                temp=temp.next
            temp.next=node
        

    
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        temp1=self.head
        temp2=self.head
        while(temp1 and temp1.next):
            temp1=temp1.next
            temp1=temp1.next
            if(temp1==None):
                break
            temp2=temp2.next
        if(self.N%2==1):
            return temp2.data
        else:
            return (temp2.data,temp2.next.data)
        


# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
#list1.push(6)
print(list1.printMiddle()) 
