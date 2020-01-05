# Node class  
class Node:

    # Function to initialise the node object  
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self) -> None:
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Function to get the middle of  
    # the linked list 
    def printMiddle(self) -> None:
        # cur = self.head
        # count = 0
        # while cur:
        #     count += 1
        #     cur = cur.next
        # mid = count // 2 + 1
        # cur = self.head
        # while count > mid:
        #     cur = cur.next
        #     count -= 1
        # print(cur.data)
        """
            Logic: The fast pointer moves two steps at time
            while the slow pointer takes one step.
            For instance if there were 50 nodes, when the fast pointer
            reaches the last node, the slow pointer would be at the 25th position.
            Time Complexity - O(n) Linear
            Since we need to go through all the elements once
            Space Complexity - O(1) Constant
            We always require only two nodes (slow and fast)
        """
        if not self.head:
            print('Invalid')
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        print(slow.data)

    def printList(self) -> None:
        cur = self.head
        result = []
        while cur:
            result.append(f'{cur.data}')
            cur = cur.next
        print(' -> '.join(result))


if __name__ == '__main__':
    # Driver code
    list1 = LinkedList()
    list1.push(5)
    list1.push(4)
    list1.push(2)
    list1.push(3)
    list1.push(1)
    list1.printList()
    list1.printMiddle()
