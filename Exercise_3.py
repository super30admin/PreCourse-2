# Time Complexity :
# Push - O(n)
# printMiddle - O(n)
# Space Complexity : O(1)
# Did this code successfully run on Leetcode :
# Any problem you faced while coding this :No

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
        # This line creates a new node with the data as given element. The second component of this nod points to None.
        new_node = Node(new_data)

        # This is the case if the linked list is empty. 
        # If the linked list is empty, we will make the new given node as the head node.
        if not self.head:
            self.head = new_node
            return 

        # This is the case if the linked list is not empty.
        # If the linked list is not empty, we will add the given element at the end of the linked list. 
        ending_node = self.head
        while ending_node.next:
            ending_node = ending_node.next
        ending_node.next = new_node
        return 
        
  
    # Function to get the middle of  
    # the linked list 
    # We will use fast pointer and slow pointer technique to find the middle of the singly linked list.
    # We will assign tow pointers to the head of the linked list. 
    # Slow pointer will move from one node to other while fast pointer will skip one node and points to the next node.
    def printMiddle(self): 
        slow = self.head
        fast = self.head
        # Loop through until fast pointer reaches the end of the list.
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data


# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.push(9) 
list1.push(13) 
print(list1.printMiddle() )
