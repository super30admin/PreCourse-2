# Node class  

# Time Complexity : o(n)
# Space Complexity : o(1)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
 
class LinkedList:
    # Function to add a new node
    def push(self, head_ref, data_val):
        # Allocate node and put in the data
        new_node = Node(data_val)
        # Link the old list off the new node
        new_node.next = head_ref
        # move the head to point to the new node
        head_ref = new_node
        return head_ref

    def printMiddle(self, head):
        if head != None:
            # find length
            len = self.getLen(head)
            temp = head
            # traverse till we reached half of length
            midIdx = len // 2
            while midIdx != 0:
                temp = temp.next
                midIdx -= 1
            # temp will be storing middle element
            print('The middle element is [%d]' % temp.data)
            

# Driver code 
head = None
list1 = LinkedList() 
list1.push(head,5) 
list1.push(head,4) 
list1.push(head,2) 
list1.push(head,3) 
list1.push(head,1) 
list1.printMiddle(head) 

#output
#2