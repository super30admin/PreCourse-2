# Node class
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

# // Time Complexity : O(n) to push the Node
# // Space Complexity : O(1) since we are not using anything
# // Did this code successfully run on Leetcode : yes
# // Any problem you faced while coding this : nope
#
# // Your code here along with comments explaining your approach
class LinkedList: 
  
    def __init__(self):
        self.head = None
        self.size = 0
        

    def push(self, new_data):
        curr = self.head
        if not curr:
            self.head = Node(new_data)
        else:
            while curr.next:
                curr = curr.next
            curr.next = Node(new_data)
        self.size += 1
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        if not self.head:
            return self.head
        curr = counter  = self.head
        size = 0
        while counter:
            counter = counter.next
            size+=1
        mid = size//2
        while mid > 0:
            curr = curr.next
            mid -= 1
        return curr

# Driver code 
list1 = LinkedList() 
list1.push(5)
list1.push(4)
list1.push(2)
list1.push(3)
list1.push(1)
middle = list1.printMiddle()
print(middle.data)

list2 = LinkedList()
middle = list2.printMiddle()
if not middle:
    print("Linked List is Empty")

list3 = LinkedList()
list3.push(2)
middle = list3.printMiddle()
print(middle.data)
