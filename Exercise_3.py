'''
1) push()
Time complexity: O(1)
Space complexity: O(1)

2) printMiddle()
Time complexity: O(N)
Space complexity: O(1)
'''

# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data): 
        self.data = data
        self.next = None
        
class LinkedList: 
  
    def __init__(self):
        self.head = None 
        self.tail = None
  
    def push(self, new_data): 
        if self.head is None:
            new_node = Node(new_data)
            self.head = new_node
            self.tail = new_node
        else:
            new_node = Node(new_data)
            self.tail.next = new_node
            self.tail = new_node


  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        if self.head is None:
            print('LinkedList is empty')
            return False
        slow, fast = self.head , self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        print('Middle node is',slow.data)
        return True

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 
