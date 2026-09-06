"""
Time Complexity: O(n) — the fast pointer traverses the list once, visiting each node at most once (in steps of 2), 
                        so it's linear in the number of nodes.
Space Complexity: O(1) — only two pointers are used regardless of list size; no extra data structures.

Did this code successfully run on Leetcode: Yes (Problem: 876. Middle of the Linked List)

Approach:
This uses the slow/fast pointer (tortoise and hare) technique:

1. Slow_pointer moves one node at a time.
2. Fast_pointer moves two nodes at a time.
3. When fast_pointer reaches the end of the list, slow_pointer will be at the middle, 
   since it has traveled half the distance.
4. This works in a single pass without needing to know the length of the list in advance.
"""


# Node class
class Node:

    # Function to initialise the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null


class LinkedList:

    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def to_list(self):
        """Helper to convert linked list to a Python list (for testing)."""
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

    # Function to get the middle of
    # the linked list
    def printMiddle(self):
        middle_value = self.get_middle()
        print("The middle element is:", middle_value)

    def get_middle(self):
        """Returns the middle element's data (or None if list is empty)."""
        slow_pointer = self.head
        fast_pointer = self.head
        if self.head is not None:
            while (fast_pointer is not None and
                   fast_pointer.next is not None):
                fast_pointer = fast_pointer.next.next
                slow_pointer = slow_pointer.next
            return slow_pointer.data
        return None


def run_tests():
    # Test 1: Odd number of elements
    # push order: 5,4,2,3,1 -> list: 1 -> 3 -> 2 -> 4 -> 5
    list1 = LinkedList()
    for val in [5, 4, 2, 3, 1]:
        list1.push(val)
    assert list1.to_list() == [1, 3, 2, 4, 5], "List construction failed"
    assert list1.get_middle() == 2, f"Expected 2, got {list1.get_middle()}"
    print("Test 1 passed: odd-length list middle =", list1.get_middle())

    # Test 2: Even number of elements
    # push order: 4,3,2,1 -> list: 1 -> 2 -> 3 -> 4
    list2 = LinkedList()
    for val in [4, 3, 2, 1]:
        list2.push(val)
    assert list2.to_list() == [1, 2, 3, 4], "List construction failed"
    # With slow/fast pointer approach, for even-length lists the
    # "middle" returned is the second of the two middle elements.
    assert list2.get_middle() == 3, f"Expected 3, got {list2.get_middle()}"
    print("Test 2 passed: even-length list middle =", list2.get_middle())

    # Test 3: Single element
    list3 = LinkedList()
    list3.push(42)
    assert list3.get_middle() == 42, f"Expected 42, got {list3.get_middle()}"
    print("Test 3 passed: single-element list middle =", list3.get_middle())

    # Test 4: Empty list
    list4 = LinkedList()
    assert list4.get_middle() is None, "Expected None for empty list"
    print("Test 4 passed: empty list returns None")

    print("\nAll tests passed!")


if __name__ == "__main__":
    # Driver code (original demonstration)
    list1 = LinkedList()
    list1.push(5)
    list1.push(4)
    list1.push(2)
    list1.push(3)
    list1.push(1)
    list1.printMiddle()

    print("\nRunning tests...\n")
    run_tests()