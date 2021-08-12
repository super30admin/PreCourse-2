# Time Complexity : O(N/2) => O(N)  as we go to the end of the list
# Space Complexity : O(1) as no extra space is used,just temporary variables like fast and slow
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No


# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):  
        self.data = data
        self.next = None
        
class LinkedList: 
  
    def __init__(self): 
        self.head = Node(None)
  
    def push(self, new_data): 
        if not self.head:
            self.head.data = new_data
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            new_node = Node(new_data)
            temp.next = new_node

    # Function to get the middle of  
    # the linked list 
    # fast pointer is twice as fast as slow pointer
    # so when fast reached end of list, slow reaches the middle
    def printMiddle(self): 
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        print(slow.data)

            
        
        

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 

list1.printMiddle()
