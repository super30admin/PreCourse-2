# Time and Space Complexity
# Space Complexity: O (N) where N denoted the number of elementes/nodes in the given LinkedList
# Time Complexity: 
# push function has the time complexity of O(1) amd space complexity of O(1)
# printMiddle function has the time complexity of O(N) and space complexity of O(1)

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
        newNode=Node(new_data)
        newNode.next=self.head
        self.head=newNode
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        slow=fast=self.head
        while fast !=None and fast.next!=None:
            fast=fast.next.next
            slow=slow.next
        print("Middle element is:",slow.data)
        return slow.data


# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 
