# Time Complexity : O(log(n))
# Space Complexity : O(log(n))
# Did this code successfully run on Leetcode : Yes, but idk how to print to ide, shows mem location when using "print" syntax
# Any problem you faced while coding this : off by one error previously
# Find Mid Point of a Singly Linked List.

# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):  
        self.data = data
        self.next = None;
        
class LinkedList: 
  
    def __init__(self): 
        self.head = None
        
  
    def push(self, new_data): 
        newNode = Node(new_data)
        newNode.next= self.head
        self.head = newNode

  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        curr = self.head
        count = 0
        while curr:
            count = count + 1
            curr = curr.next
        mid = count // 2
        #point to head again
        curr = self.head
        for i in range(mid):
            curr = curr.next

        return curr

    def printLinkedList(self):
        node = self.head
        while node != None:
            print(node.getData())
            node = node.getNext()


# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle()

