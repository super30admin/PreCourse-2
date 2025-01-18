#Time Complexity: O(n)
#Space Complexity: O(1)
# by using Floyd's Cycle Finding Algorithm
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
        new_node.next = self.head  # Link the new node to the current head
        self.head = new_node # Update the head to the new node
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        slow = self.head  # Slow pointer
        fast = self.head  # Fast pointer

        # Traverse the list
        while fast is not None and fast.next is not None:
            slow = slow.next         
            fast = fast.next.next

        # Slow pointer now points to the middle node
        if slow:
            print("The middle element is:", slow.data)
        else:
            print("The list is empty.")

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 
