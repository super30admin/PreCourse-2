# Time complexity : O(n)
# Space Complexity : O(1)

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
        if self.head is None:
            self.head = new_node
        else:
            current =  self.head
            
            while current.next:
                current = current.next
            current.next = new_node
        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        if self.head is None:
            print("The list is empty")
            return

        slow = self.head
        fast = self.head

        # Fast pointer moves two steps, slow pointer moves one step
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        print("The middle element is:", slow.data)
# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 
