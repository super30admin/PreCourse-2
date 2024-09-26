# Node class
# time complexity: O(n)
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):  
        self.data = data
        self.next = None
class LinkedList: 
    def __init__(self): 
        self.head = None
  
    def push(self, new_data): 
        # if head not present, make head
        if self.head is None:
            self.head = Node(new_data)
        else:
            #create new node and update next of new node to old head
            node = Node(new_data)
            node.next = self.head
            self.head = node

    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        # if no head, 1 element or 2 elements in linked list, no middle, return none
        if self.head is None or self.head.next is None or self.head.next.next is None:
            return None
        # slow moves 1 step , fast moves 2 step
        # when fast is at the end, slow is at the mid
        slow = self.head
        fast = self.head
        while fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        print(slow.data)
        return slow.data

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 
