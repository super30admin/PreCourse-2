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
        newNode = Node(new_data)
        if self.head is None:
            self.head = newNode
            return
        
        curr = self.head
        while curr.next:
            curr = curr.next
        
        curr.next = newNode
  
    # Function to get the middle of the linked list 
    # Time Complexity: O(N)
    # Space Complexity: O(1)
    def printMiddle(self): 
        # Empty linked list has no middle
        if self.head is None:
            print(None)
            return None
        
        # Initialize two pointers, one running slow (1-step)
        # and another running fast (2-step). When 'fast' reached end of linked list,
        # 'slow' will point to the middle of the linked list.
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        print(slow.data)
        return slow

# Driver code 

# Case 1
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 

# Case 2
list2 = LinkedList() 
list2.push(5) 
list2.push(4) 
list2.push(2) 
list2.push(3) 
list2.push(1) 
list2.push(0) 
list2.printMiddle() 

# Case 3
list3 = LinkedList() 
list3.printMiddle() 

# Case 4
list4 = LinkedList() 
list4.push(1)
list4.printMiddle() 

# Case 5
list5 = LinkedList() 
list5.push(1)
list5.push(2)
list5.printMiddle() 