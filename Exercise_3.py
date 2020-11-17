#  Time Complexity : push :O(N) printMiddle: O(N/2)
#  Space Complexity : O(N)
#  Did this code successfully run on Leetcode : yes
#  Any problem you faced while coding this : No



# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):  
        self.data = data
        self.next = None
        
class LinkedList:  
    def __init__(self): 
        self.list = None
  
    def push(self, new_data): 
        if self.list == None:
            self.list = Node(new_data)
            return
         
        ptr = self.list
        while ptr.next!=None:
            ptr = ptr.next
        ptr.next = Node(new_data)
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        ptr = self.list
        ptrslow = self.list

        while ptr.next != None and  ptr.next.next != None:
            ptr = ptr.next.next
            ptrslow = ptrslow.next
        print(ptrslow.data)

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 

'''
approch : slow and fast pointer 
'''