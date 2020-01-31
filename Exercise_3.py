# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):
        self.value = data
        self.next = None
        
class LinkedList: 
  
    def __init__(self):
        # Instead of tracking only head, we can track tail node and length for better optimization
        self.head = None
        self.length = 0
        self.tail = None
  
    def push(self, new_data):
        # update tail node and length along with head node to make push in O(1) time
        # O(1) Time Complexity | O(1) Space Complexity
        if self.head == None:       # check for a corner case and update length as well
            self.length = 1
            self.head = Node(new_data)
            self.tail = self.head
        else:                       # a normal push operation in constant time
            self.length += 1
            curr_node = Node(new_data)
            self.tail.next = curr_node
            self.tail = curr_node
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        # O(n) Time Complexity | O(1) Space Complexity

        if (self.length % 2 != 0):      # if length is odd, print only one element
            mid_id = int(self.length / 2)
            curr_node = self.head
            cnt = 1
            while (cnt < mid_id):
                curr_node = curr_node.next
                cnt += 1
            print(curr_node.next.value)

        else:                           # if length is even, print 2 middle elements
            mid_id = int(self.length / 2)
            curr_node = self.head
            cnt = 1
            while (cnt < mid_id):
                curr_node = curr_node.next
                cnt += 1
            print(curr_node.value, curr_node.next.value)

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1)
list1.printMiddle() 
