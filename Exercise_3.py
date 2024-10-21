# Time Complexity: O(n) - We traverse the list only once to find the middle element.
# Space Complexity: O(1) - No extra space is used apart from a few variables.
# Did this code successfully run on Leetcode? 
# Yes, works for similar problems.
# Any problem you faced while coding this: 
# No issues encountered.

# Your code here along with comments explaining your approach:
# - To find the middle of the linked list, we use the **two-pointer technique**:
#   - One pointer (slow) moves **one step** at a time.
#   - Another pointer (fast) moves **two steps** at a time.
# - When the fast pointer reaches the end, the slow pointer will be at the middle.

# Node class  
class Node:
    """A node in a singly linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        """Initialize the head of the linked list."""
        self.head = None

    def push(self, new_data):
        """
        Insert a new node at the beginning of the list.
        Takes O(1) time.
        """
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printMiddle(self):
        """
        Function to print the middle element of the linked list.
        Uses the two-pointer technique.
        """
        slow = self.head  # Slow pointer
        fast = self.head  # Fast pointer

        # Move fast pointer two steps and slow pointer one step at a time
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        # Slow pointer now points to the middle node
        if slow is not None:
            print(f"The middle element is: {slow.data}")

# Driver code 
list1 = LinkedList()
list1.push(5)
list1.push(4)
list1.push(2)
list1.push(3)
list1.push(1)
list1.printMiddle()
