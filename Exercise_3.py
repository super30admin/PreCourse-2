
# Time Complexity: O(n) - to traverse the list to find the mid element
# Space Complexity O(1) 
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No
# For even length, returns the second middle node.

class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data=None, nxt=None):  
        self.nxt = nxt
        self.data = data

        
class LinkedList: 
  
    def __init__(self): 
        self.head = None
        self.cnt = 0

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.nxt = self.head
        self.head = new_node
        self.cnt = self.cnt + 1         # if i delete the data from the linkedlist, we should decrement the count

  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        if self.head is None:
            return None
        
        slow = self.head
        fast = self.head

        while fast is not None and fast.nxt is not None:
            slow = slow.nxt
            fast = fast.nxt.nxt
        
        return slow.data

    
        # curr = self.head
        # mid = self.cnt // 2
        # while curr is not None:
        #     if mid == 0:
        #         print(curr.data)
        #         return curr.data
            
        #     mid = mid - 1
        #     curr = curr.nxt

        # return None

    def to_list(self):
        curr = self.head
        result = []
        while curr is not None:
            result.append(curr.data)
            curr = curr.nxt

        return result


list1 = LinkedList() 
assert list1.printMiddle() == None
list1.push(5) 
assert list1.printMiddle() == 5

list1.push(4) 
assert list1.printMiddle() == 5

list1.push(30) 
list1.push(10) 
assert list1.printMiddle() == 4

list1.push(3) 
list1.push(1) 
assert list1.printMiddle() == 30


list1.push(1) 
assert list1.printMiddle() == 10


# Driver code (S30 original)
list1 = LinkedList()
list1.push(5)
list1.push(4)
list1.push(2)
list1.push(3)
list1.push(1)
list1.printMiddle()


# Tests: fresh list per case
def build(*values):
    ll = LinkedList()
    for v in values:
        ll.push(v)
    return ll


# push order
assert build(5, 4, 2, 3, 1).to_list() == [1, 3, 2, 4, 5]

# empty
assert build().printMiddle() is None

# single node
assert build(7).printMiddle() == 7

# two nodes: 1 -> 2, second middle
assert build(2, 1).printMiddle() == 2

# three nodes: 1 -> 2 -> 3
assert build(3, 2, 1).printMiddle() == 2

# four nodes: 10 -> 30 -> 4 -> 5, second middle
assert build(5, 4, 30, 10).printMiddle() == 4

# five nodes (S30 driver): 1 -> 3 -> 2 -> 4 -> 5
assert build(5, 4, 2, 3, 1).printMiddle() == 2

# six nodes: 60 -> 50 -> 40 -> 30 -> 20 -> 10
assert build(10, 20, 30, 40, 50, 60).printMiddle() == 30

print("all tests pass")