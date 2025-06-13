 #Space Complexity: O(n)
 # Node class
class Node:
    # Function to initialise the node object  
    def __init__(self, data):
        self.data=data
        self.next=None
        
class LinkedList:
    def __init__(self):
        self.head=Node(None)
        self.tail=self.head

    def push(self, new_data):
        #Time Complexity: O(1)
        self.tail.next=Node(new_data)
        self.tail=self.tail.next

    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        #Time Complexity: O(n)
        slow=self.head
        fast=self.head

        while fast:
            fast=fast.next.next
            slow=slow.next

        return slow.data

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
print(list1.printMiddle())
