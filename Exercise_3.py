# Time complexity : O(n/2). If n is the length of linked list, 
#we update the slow pointer n/2 times to reach the middle of the linked list
# Space complexity : O(n) where n is the number of nodes in the list

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
        newNode = Node(new_data)
        # While adding element to the list for the first time, 
        # just update the head and tail pointers to the new node
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = self.tail.next

  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        # Maintain 2 pointers: slow and fast, both initialized to head pointer
        # Slow pointer updates one step at a time and 
        # fast pointer updates 2 steps at a time. Slow pointer 
        # will be at the middle of the linked list when 
        # fast pointer reaches the end.

        slow = self.head; fast = self.head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        print(f'Middle Element: {slow.data}')


# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 
