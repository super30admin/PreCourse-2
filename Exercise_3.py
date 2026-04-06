# // Time Complexity : O(n)
# // Space Complexity : O(n)
# // Did this code successfully run on Leetcode :
# // Any problem you faced while coding this :


# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data, next=None):  
        self.data = data 
        self.next = next 
class LinkedList: 
  
    def __init__(self): 
        self.head = None
  
    def push(self, new_data): 
        newNode = Node(new_data)
        if self.head is None:
            self.head = newNode 
        else:
            # 1->2
            cur = self.head 
            while cur.next:
                cur = cur.next 

            cur.next = newNode 
  
  # 1->2->3->4->5
  #       t     h 
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        tort = self.head 
        hare = self.head 
        while hare and hare.next:
            hare = hare.next.next 
            tort = tort.next

        return tort 

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 
