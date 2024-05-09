# Time Complexity : O(n) as the function has to traverse the LL only once
# Space Complexity : O(1) constant space
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : Only one. If there are even number of nodes added to the Linked List, it is not clear which element should be returned.

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
    def printMiddle(self): # using the two pointer method to traverse the linked list and get the mid point. This method is more efficient as it has to go through the LL only once
        if self.head is None:
            print("Empty Linked List")
            return
        # Both fast and slow at the head
        slow = self.head
        fast = self.head

        while fast is not None and fast.next is not None:
            # Slow jumps one node while fast jumps two. When fast or fast.next becomes None, fast pointer will be at the end of the LL, but the slow pointer will be half way there i.e in the middle
            slow = slow.next
            fast = fast.next.next

        print("The mid-point of the singly linked list is : ", slow.data)

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1)
list1.push(35) 
list1.push(44) 
list1.push(22) 
list1.push(35) 
list1.push(111)
list1.push(65) 
list1.push(47) 
list1.push(20) 
list1.push(30) 
list1.push(16) 
list1.push(56) 
list1.push(784) 
list1.push(25) 
list1.push(35) 
list1.push(16) 
list1.push(577) 
list1.push(400) 
list1.push(2767) 
list1.push(39) 
list1.push(19) 
list1.push(59) 
list1.push(44) 
list1.push(256) 
list1.push(376) 
list1.push(100) 
list1.printMiddle() 
