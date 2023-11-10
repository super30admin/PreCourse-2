"""
Leetcode: https://leetcode.com/problems/middle-of-the-linked-list/ (similar) - not submitted
TC/SC - see below
Challenge - Finding middle for even and odd length of linked list. Also, corner cases of empty list.
"""


# Node class
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):  
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # TC - O(N), SC - O(1)
    def push(self, new_data):
        # when no head found, assign head
        if self.head is None:
            self.head = Node(new_data)
        else:
            #  find the last node and append a new node to it
            curr = self.head
            while curr and curr.next:
                curr = curr.next
            newNode = Node(new_data)
            curr.next = newNode
  
    # Function to get the middle of  
    # the linked list
    # TC - O(N/2), SC - O(1)
    def printMiddle(self):
        if self.head is None:
            print('no middle found in empty list.')
        else:
            slow, fast = self.head, self.head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next

            print(slow.data)


# Driver code 
list1 = LinkedList() 
list1.push(5)
list1.push(4)
list1.push(2)
list1.push(3)
list1.push(1)
list1.printMiddle()

"""
Logic - 

# slow is mid when fast.next is None
1 -> 2 -> 3 -> 4 -> 5
1:
    s    
          f
2:
          s 
                    f           

# slow is mid when fast is None
1 -> 2 -> 3 -> 4
1:
     s
          f
2:
          s
                   f          

Common - fast = None or fast.next = None
"""
