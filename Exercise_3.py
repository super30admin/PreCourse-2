# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):
        self.data = data
        self.next = None
    

#let's say our linked list has 5 nodes
# the middle will be the third node
# if our linked list has 4 nodes, the middle is node 2
# one way can be to loop through the end, keep a count and then again loop from begining to the middle node (this is brute force method with O(n) time complexity)
# other method is we have slow and fast pointers.
# the slow pointer will move to every next node and the fast pointer will move every two nodes.
# when the fast pointer will point to null, we will know that the position where the slow pointer is, that is the middle. We return that
class LinkedList: 
  
    def __init__(self): 
        self.head = None
        
        
    def push(self, new_data): 
        newNode = Node(new_data)

        if not self.head:
            self.head = newNode
        else:
            curr = self.head
            while curr.next != None:
                curr = curr.next
            curr.next = newNode

       

        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        if not self.head:
            return -1
        
        slow, fast = self.head, self.head

        while (fast.next != None):
            slow = slow.next
            fast = fast.next.next
        
        print (slow.data)



# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 
