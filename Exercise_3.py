# Overall time complexity: O(n/2)
# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data): 
        self.data = data
        self.next = None

class LinkedList: 
  
    def __init__(self):
        # initailize the head node
        self.head = None
  
    # add new node to the linked list
    def push(self, new_data):
        # insert at the beginning of the list
        # create a Node with new_data
        new_n = Node(new_data)
        # point the new node to head
        new_n.next = self.head
        # make the new node the head of the list
        self.head = new_n
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        # point the slow_ptr and fast_ptr to the head of the list
        slow_ptr = self.head
        fast_ptr = self.head
        # check if the list is empty or not
        if self.head is not None:
            # check if fast_ptr and fast_ptr.next has reached the end of list or not
            while(fast_ptr is not None and fast_ptr.next is not None):
                # increment the fast_ptr by 2
                fast_ptr = fast_ptr.next.next
                # increment the slow_ptr by 1
                slow_ptr = slow_ptr.next
            # print the slow_ptr data which is the middle element of the linked list
            print(slow_ptr.data)

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 
