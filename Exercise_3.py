# Time Complexity : O(n)
# Space Complexity : O(1)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No problem 

# Your code here along with comments explaining your approach : Traverse the linked list 
# with 2 pointers starting at the same point. One pointer iterates over each element and 
# other over alternate elements. the one iterating over alternate element moves 2 times 
# faster and hence will reach the end of the list faster and at the same time slower pointer
# reaches the middle of the list 


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
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
  
    # Function to get the middle of  
    # the linked list 

    def printMiddle(self): 
        slow = self.head
        fast = self.head
  
        if self.head is not None:
            while (fast is not None and fast.next is not None):
                fast = fast.next.next
                slow = slow.next

            print("The middle element is: ", slow.data)

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(0) 
list1.push(8)
list1.push(100)
list1.push(5)
list1.push(6)
list1.printMiddle() 
