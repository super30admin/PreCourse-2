# Time Complexity : O(n), where n is the length of the list
# Space Complexity : O(1)
# Did this code successfully run on Leetcode : N.A.
# Any problem you faced while coding this : No

# Your code here along with comments explaining your approach
class Node:
    # Function to initialise the node object  
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self): 
        self.head = None

    # Adding to the head of the list.
    def push(self, new_data):
        toAdd = Node(new_data)
        toAdd.next = self.head
        self.head = toAdd

    # implemented using Floyd's slow and fast pointers approach, fast
    # pointer reaches the end of the list the slow is at the middle.
    def printMiddle(self):
        if self.head == None:
            print("The list is empty")
            return

        slow = self.head
        fast = self.head

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        print(slow.data)

# Driver code 
list1 = LinkedList()
# list1.push(6)
list1.push(5)
list1.push(4)
list1.push(3)
list1.push(2)
list1.push(1)
list1.printMiddle() 
