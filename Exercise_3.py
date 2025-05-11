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
        n = Node(new_data)
        if self.head is None:
            self.head = n
            self.tail = n
        else:
            self.tail.next = n
            self.tail = n

    def printList(self):
        itr = self.head
        while itr:
            print('%s->'%(itr.data),end='')
            itr = itr.next
        print('NULL')
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        slow = self.head
        fast = self.head
        while fast != None and fast.next != None: 
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
list1.printList()
list1.printMiddle() 
