# Time Complexity : Approach 1: O(N) iterates over the list twice, once for finding the length and second for mid (N + N/2)
# Approach 2: O(N) iterates over the list only N/2 times
# Space Complexity : O(N) / size of linkedlist
# Exercise_3 : Find Mid Point of a Singly Linked List.

# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList: 
    
    # Initialize the LinkedList head node
    def __init__(self): 
        self.head = None
  
    def push(self, new_data):
        newNode = Node(new_data)
        if not self.head:
            self.head = newNode
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = newNode

    def printList(self):
        current = self.head
        listitems = []
        while current:
            listitems.append(current.data)
            current = current.next
        print(listitems)

    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        # Approach 1: Find length of linkedlist and return mid requires O(N) time
        length = 0 
        current = self.head
        while current:
            length += 1
            current = current.next
        mid = length//2
        # Iterate over list again till mid and print data
        current = self.head
        for _ in range(mid):
            current = current.next
        print(current.data)
    
    def printMiddle2(self):
        # Approach 2: Two pointers fast and slow, where fast pointer skips 2 node and slow pointer moves forward one step
        # When fast pointer reaches end of the list, slow pointer is at mid, this approach only one pass over the list and reduce time in half
        # N/2 iterations, time complexity O(N)
        p1,p2 = self.head, self.head
        while p2.next:
            p2 = p2.next
            p1 = p1.next
            if p2.next:
                p2 = p2.next
        print(p1.data)


# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1)
# list1.push(0)
list1.printList()
list1.printMiddle()
list1.printMiddle2() 
