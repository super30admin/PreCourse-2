# Exercise_3 : Find Mid Point of a Singly Linked List.

# Assumption: Array is sorted in ascending order
# Time Complexity: O(N), N = number of nodes in the linked list
# Space Complexity: O(N) to create the linked list, O(1) for slow and fast pointers
# Successful Run on Leetcode: Yes (https://leetcode.com/problems/middle-of-the-linked-list/)
# Challenges: None

# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):  
        #intialize linked list
        self.data = data
        self.next = next

        
class LinkedList: 
  
    def __init__(self):
        # initialize an empty linked list
        self.head = None
        
    def push(self, new_data): 
        # initialize a newNode with the new_data
        newNode = Node(new_data)
        # if head is None, then set the newNone as the head
        if not self.head:
            self.head = newNode
        # otherwise move the pointer to the end of the linked list and add the newNode there
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = newNode
  
    # Function to get the middle of the linked list 
    def printMiddle(self): 
        # set a slow pointer that moves one step at a time, and a fast pointer that moves two steps at a time
        # when the fast pointer reaches the end of the linked list, the slow pointer will reach the middle of the linked list
        # set a slow and fast pointer to point to the head of the linked list
        slow = fast = self.head
        # taking into account even and odd number of nodes in the linked list, move the slow pointer to the next node and the fast pointer to the next to next node
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # when we reach the end of the linked list, the slow pointer will point to the middle of the linked list
        # return the data of the slow pointer
        return slow.data

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 
