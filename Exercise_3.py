# Time Complexity: O(N/2)
# Space Complexity: O(1)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

# Node class
class Node:

    # Function to initialise the node object
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def push(self, new_data):
        current = self.head
        if current:
            while current.next:
                current = current.next
            current.next = Node(new_data)
        else:
            self.head = Node(new_data)

    # Function to get the middle of
    # the linked list
    def printMiddle(self):
        current = self.head
        fast = self.head

        while fast and fast.next:
            current = current.next
            fast = fast.next.next
        print(current.data)

    # Initial Approach for 2 pointer
    # def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     current = head
    #     fast = head
    #     while fast.next:
    #         if fast.next.next:
    #             current = current.next
    #             fast = fast.next.next
    #         else:
    #             current = current.next
    #             break
    #     return current

    # Naive Approach
    # def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     current = head
    #     mid:int = (self.getLen(current) // 2) + 1
    #     for i in range(mid-1):
    #         current = current.next
    #     return current

    # def getLen(self, curr: Optional[ListNode]) -> int:
    #     count:int = 0
    #     while curr:
    #         curr = curr.next
    #         count+=1
    #     return count

# Driver code
list1 = LinkedList()
list1.push(5)
list1.push(4)
list1.push(3)
list1.push(2)
list1.push(1)
list1.printMiddle()