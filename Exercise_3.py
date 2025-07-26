# Node class  

# Time Complexity :
#    push(x)       -> O(1)
#    printMiddle() -> O(n)
#  Space Complexity : O(1) extra (besides the O(n) list storage)
#  Did this code successfully run on Leetcode : N/A (practice / template code)
#  Any problem you faced while coding this :
#    - For even-length lists, the slow/fast pointer method returns the *second* middle.
#    - Remember to handle the empty-list case.

class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):  
        self.data = data
        self.next = None
        
class LinkedList: 
  
    def __init__(self): 
        self.head = None
  
    def push(self, new_data): 
          """
        Insert at the head. O(1)
        """
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        """
        Prints the middle node's data using slow/fast pointers.
        O(n) time, O(1) space.
        For even length, this returns the second middle element.
        """
        if self.head is None:
            print("The list is empty.")
            return

        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        print("The middle element is:", slow.data)

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 
