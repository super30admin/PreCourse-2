"""
printMiddle - 
Time Complexity : O(n)
Space Complexity : O(n)

printMiddle_2ptr - 
Time Complexity : O(n)
Space Complexity : O(1)
"""

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
        if not self.head:
            self.head = Node(new_data)
        else:
            temp = self.head
            
            while temp.next:
                temp = temp.next
            
            temp.next = Node(new_data)
            temp = temp.next 
                
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        if self.head:
            lis = [self.head]
            while lis[-1].next:
                lis.append(lis[-1].next)
            length = len(lis)
            return lis[length//2].data
        return None
    
    def printMiddle_2ptr(self):
        if self.head:
            slow = fast = self.head

            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next 
            return slow.data 
        return None 
            

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
print(list1.printMiddle())
print(list1.printMiddle_2ptr())
