#!/usr/bin/env python
# coding: utf-8

# In[19]:


# Node class  
class Node:    
    # Function to initialise the node object  
    def __init__(self, data): 
        self.data = data
        self.next = None
        return        
class LinkedList:   
    def __init__(self): 
        self.head = None
        self.size = 0
    def push(self, new_data): 
        new_node = Node(new_data)
        if self.head is None:
            self.size += 1
            self.head = new_node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node
        self.size += 1
        return 
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        if self.head is None:
            return
        if self.size % 2 == 0:
            mid = int(self.size //2)
        else:
            mid = int((self.size + 1)/2)
        
        cur = self.head
        for _ in range(mid-1):
            cur = cur.next
        return print(cur.data, mid)           
    def length(self):
        return self.size
    
    def printlist(self):
        cur = self.head
        for _ in range(self.size):
            if not cur:
                return
            print(cur.data)
            cur = cur.next
            
# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1)
list1.push(0)
list1.printMiddle() 

