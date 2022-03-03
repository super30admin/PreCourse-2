# TC: push O(N), Middle O(N/2)
# SC: push O(N), Middle(1)

# Node class  
from typing import Counter


class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):  
        self.data = data
        self.next = None
class LinkedList: 
  
    def __init__(self): 
        self.head = None
        self.counter = 0
        
  
    def push(self, new_data): 
        newNode = Node(new_data)
        if self.head == None:
            self.head = newNode
            self.counter += 1
        else:
            curr = self.head
            for i in range(self.counter):
                if curr.next == None:
                    curr.next = newNode
                    self.counter += 1
                else:
                    curr = curr.next
                    self.counter+=1
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        curr = self.head 
        mid = self.counter // 2
        if mid in [0,1]: return print(curr.data)
        for i in range(mid):
            if i + 1 == mid:
                return print(curr.data)
            else: curr = curr.next
# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 
