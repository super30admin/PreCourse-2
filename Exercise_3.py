
# Time Complexity: O(n)
# Space Complexity: O(1)

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
        if self.head is None:
            self.head = Node(new_data)
        else:
            temp = self.head
            while temp and temp.next:
                temp = temp.next
                print("WHILE: ", temp.data)
            temp.next = Node(new_data)
            temp = temp.next
            temp = Node(new_data)
            print("PUSHED: ", temp.data)
        
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        slow = fast = self.head
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
print(list1.printMiddle() )
