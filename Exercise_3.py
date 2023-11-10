# time complexity: O(N) since traversing the linked-list once 
# space complexity: O(1) since using only constant extra space
# approach: use two pointer technique- slow and fast. 
# both start from head and slow moves one node while fast moves two nodes each time.

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
        if(self.head):
            current = self.head
            while(current.next):
                current = current.next
            current.next = new_node
        else:
            self.head = new_node


        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow=slow.next
            fast = fast.next.next
        print(slow.data)

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1)
list1.printMiddle() 
