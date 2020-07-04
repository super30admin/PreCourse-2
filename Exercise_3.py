# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):  
        self.data = data
        self.next = None

class LinkedList: 
  
    def __init__(self): 
        self.head = None
  
    def push(self, new_data): 
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        if self.head is None:
            print("The singly linked list is empty")
        elif self.head.next is None:
            print("The middle point of singly linked list: ", self.head.data)

        else:
            slow_ptr, fast_ptr = self.head, self.head
            while fast_ptr is not None and fast_ptr.next is not None:
                slow_ptr = slow_ptr.next
                if fast_ptr.next is not None:
                    fast_ptr = fast_ptr.next.next
                else:
                    break

            print("The middle point of the singly linked list: ", slow_ptr.data)



# Driver code 
list1 = LinkedList() 
list1.push(5)
list1.push(4)
list1.push(2)
list1.push(3)
list1.push(1)
list1.printMiddle() 
