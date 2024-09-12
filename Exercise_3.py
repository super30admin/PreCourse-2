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
 
    def printList(self):
        node = self.head
        while node:
            node = node.next
        print("NULL")
 
    def printMiddle(self):
        
        slow = self.head
        fast = self.head
 
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
         
        print("The middle element is ", slow.data)
 

llist = LinkedList()


llist.push(1)
llist.push(2)
llist.push(3)
llist.push(4)
llist.printMiddle()