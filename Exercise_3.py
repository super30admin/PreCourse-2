# Time Complexity : push -> O(1), print_middle -> O(n)
# Space Complexity : push -> O(n), print_middle -> O(1)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):
        self.data=data
        self.next=None

        
class LinkedList: 
  
    def __init__(self): 
        self.head = Node(None)
        
  
    def push(self, new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node 
        
  
    # Function to get the middle of  
    # the linked list 
    def print_middle(self):
        if not self.head:
            return self.head
        slow=self.head
        fast=self.head
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
        return slow 


# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1)
print(list1.print_middle().data)
