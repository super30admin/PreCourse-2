# Time Complexity : O(n)
# Space Complexity : O(n)
# Did this code successfully run on Leetcode : not a problem on leetcode
# Any problem you faced while coding this : no

# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):  
        self.data = data
        self.next = None

class LinkedList: 
  
    def __init__(self): 
        self.head = None      
  
    def push(self, new_data): 
        if self.head == None:
            self.head = Node(new_data)
        temp = Node(new_data)
        temp.next = self.head
        self.head = temp
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        count = 0
        temp = self.head
        if temp == None:
            return None
        else:
            while temp.next:
                temp = temp.next
                count = count+1
        count1 = 0
        temp1 = self.head
        while temp1.next:
            if count1 == count//2:
                return print(temp1.data)
            else:
                count1 = count1+1
                temp1 = temp1.next

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1)
list1.printMiddle() 
