# Node class  
#Time Complexity :  O(n)
#Space Complexity : O(n)
#Did this code successfully run on Leetcode : yes
#Any problem you faced while coding this : no


class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):  
        self.data = data
        self.next = None
        
class LinkedList: 
  
    def __init__(self): 
        self.head = None
        
  
    def push(self, data): 
        if self.head:
            current = self.head
            while current.next :
                current = current.next
            current.next = Node(data)
        else:
            self.head = Node(data)
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        if self.head:
            temp1 = self.head
            temp2 = self.head
            while temp2 and temp2.next:
                temp1 = temp1.next
                temp2 = temp2.next.next
            return temp1.data
        else:
            return

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
middle_element = list1.printMiddle() 
print("middle element is {}".format(middle_element))
