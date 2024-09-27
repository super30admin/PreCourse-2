"""

  Student : Shahreeen Shahjahan Psyche

  Memory Complexity: O(N)

  The Code Ran Successfully

"""
# Node class
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList: 
  
    def __init__(self):
        self.head = None


    # Running Complexity : O(N)
    def push(self, new_data):
        new_node = Node(new_data)
        if self.head == None:
            self.head = new_node
        else:
            current = self.head
            while(current is not None):
                if current.next is None:
                    current.next = new_node
                    break
                current = current.next
  
    # Function to get the middle of  
    # the linked list

    # Running Complexity : O(N)
    def printMiddle(self):

        if self.head == None:
            return

        if self.head.next is None:
            print(self.head.data)
            return
        fast = self.head
        slow = self.head

        while(fast.next is not None):
            fast = fast.next.next
            slow = slow.next
        print(slow.data)


# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 
