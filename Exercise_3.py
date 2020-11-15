# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):  
        self.data = data
        self.next = None
        
class LinkedList: 
  
    def __init__(self): 
        self.head = None
        
  
    def push(self, new_data): # Time - O(1)
        if self.head is None:
            self.head = Node(new_data)
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = Node(new_data)
        
  
    # Function to get the middle of  
    # the linked list 
    """
    Time - O(n)
    Space - O(1)
    Idea - When the fast pointer reaches None the slow pointer will be pointing to middle
    """
    def printMiddle(self): 
        if self.head is None:
            print("List is empty")
            return

        slow = fast = self.head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next
            if fast.next is not None:
                fast = fast.next

        print(slow.data)


# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 
