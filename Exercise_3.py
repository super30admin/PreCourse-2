

# Time Complexity: O(n) — Traverse through list
# Space Complexity: O(1) — For two pointers (slow, fast)


# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data): 
        self.data = data 
        self.next = None
        
class LinkedList: 
  
    def __init__(self): 
        self.head = None   # Initialize head to None
        
  
    def push(self, new_data):   # Adding elements to front of list as in .java file
        newNode = Node(new_data)      # Create new node
        newNode.next = self.head      # Point to old head
        self.head = newNode           # Mark newNode as new head
        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        slow = self.head        # slow moves once
        fast = self.head        # fast moves twice

        if self.head is None:
            print("Empty list")
            return

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

         # As fast reaches end, slow is at middle and return
        print("Middle of linked list is ", slow.data)
                  


if __name__=="__main__":
# Driver code 
    list1 = LinkedList() 

    # To get -  1 -> 3 -> 2 -> 4 -> 5
    list1.push(5) 
    list1.push(4) 
    list1.push(2) 
    list1.push(3) 
    list1.push(1)
    list1.printMiddle()  # Middle of linked list is 2
