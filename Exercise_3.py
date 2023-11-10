# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):  
      self.data = data
      self.next = None

class LinkedList: 
  
    def __init__(self): 
        self.head = Node(0)
        self.length = 0

    """
    Push will take O(n) time to add new element to the linked list
    """
    def push(self, new_data):
        curr = self.head

        while curr.next:
            curr = curr.next
        
        curr.next = Node(new_data)
        self.length += 1

  
    # Function to get the middle of  
    # the linked list
    """
    printMiddle will take O(n/2) i.e O(n) time to print the middle element.
    """
    def printMiddle(self): 
        mid = self.length // 2
        curr = self.head
        for _ in range(mid+1):
            curr = curr.next
        print(curr.data)


# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 
