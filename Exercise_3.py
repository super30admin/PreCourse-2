# Time Complexity : 
# Space Complexity: 
# Did you find this problem on Leetcode: Yes
# Did you face any problem solving it: Logic used for printMiddle function 

# Problem solving approach: Traverse linked list using two pointers. To get the middle value used fast and
# slow pointer, when fast will reach the end element, slow will reach the middle element.

# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data): 
        self.data = data                                # Assigned data
        self.next = None                                # Initialized next as null
        
class LinkedList:                                       # LinkedList class contains node object
  
    def __init__(self):
        self.head = None
  
    def push(self, new_data):                           # Push function will add a new node at start
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node 
        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        print("Element in the middle is ",slow.data) 

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 
