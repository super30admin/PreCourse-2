'''
// Time Complexity : O(N)
// Space Complexity :  O(1)
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : Thought approaches like counting, having additional pointer 


// Your code here along with comments explaining your approach
'''

'''
- Iterate with two pointers [one slow or regular speed another one double the speed], 
- When faster reaches end , return slow's node which is center
'''

# Node class  
class Node:  
    # Function to initialise the node object  
    def __init__(self, data): 
        self.data=data
        self.next=None

        
class LinkedList: 
  
    def __init__(self): 
        self.head=None
  
    def push(self, new_data): 
        if self.head is None:
            self.head=Node(new_data)
        else:
            node=self.head
            while node.next is not None:
                node=node.next
            
            node.next=Node(new_data)
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        slow=fast=self.head

        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
        
        return slow.data

'''
    5-4-2-3-1-7
'''

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.push(7) 
print(list1.printMiddle() )
