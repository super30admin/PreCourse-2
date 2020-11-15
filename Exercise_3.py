# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):  
        self.data = data
        self.next = None

class LinkedList: 
  
    def __init__(self): 
        self.head = Node(None)
        self.curr = self.head

    def push(self, new_data): 
        self.curr.next = Node(new_data)
        self.curr = self.curr.next
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        slow = fast = self.head.next

        while True:
            if fast == None or fast.next == None :
                break
            else:
                slow = slow.next
                fast = fast.next.next
        print("Middle is: ", slow.data)

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1)
list1.push(6)
list1.printMiddle() 
