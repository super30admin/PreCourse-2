# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):  
        self.data = data
        self.next = None
class LinkedList: 
  
    def __init__(self):
        # This can be considered as a sentinel node or dummy node, the actual nodes can be appended to this node
        self.head =  Node(None)
        # size variable to keep track of the length of the linked list
        self.size = 0
        
  
    def push(self, new_data):
        # increment the size and append to the frot of the linked list
        self.size += 1
        _node = Node(new_data)
        _node.next = self.head
        self.head = _node
        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        # find the length of the linked list
        # and iterate through the list again to see if we have reached count length/2
#       # or we can maintain a self.size variable to keep track of count of elements added
        temp = self.head
        count = 0
        # we are using temp.next in while loop as we have the sentinel node used in constructor
        while(temp.next):
            if count == self.size//2:
                print(temp.data)
                break
            count += 1
            temp = temp.next
        # if there is no middle element, that is size is zero, return None
        return None



# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1)
# to add odd number of elements once to verify
list1.push(8)
list1.printMiddle() 
