# Time complexity: O(n)
# Space complexity: O(1)

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
        node = Node(new_data)
        if self.head.data is None:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node
        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        """
        Keep two pointers. Iterate first one by one node and the second one by two nodes at a time.
        When the second pointer reaches the last node, the first pointer will reach the middle node.
        """
        slowPointer = self.head
        fastPointer = self.head
        while fastPointer and fastPointer.next:
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next.next
        print(slowPointer.data)

            
# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
# list1.push(0) 
list1.printMiddle() 
