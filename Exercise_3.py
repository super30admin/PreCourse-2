class Node:  
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
  
    def printMiddle(self): 
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        if slow:
            print(f"The middle element is: {slow.data}")
        else:
            print("The list is empty.")

list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle()
