
# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: Take two pointers, fast and slow. Traverse the linked list by making fast pointer move by two and slow pointer by one.
# When fast pointer reaches end of linked list, slow pointer will at the middle of linked list.

# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):  
        self.next = None
        self.data = data
        
class LinkedList: 
  
    def __init__(self): 
        self.head = None
        
  
    def push(self, new_data): 
        newNode = Node(new_data)
        newNode.next = self.head
        self.head = newNode
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        slow = self.head
        fast = self.head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        print("Middle element is ", slow.data)


# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 
