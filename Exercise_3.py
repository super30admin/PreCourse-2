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
        # Time Complexity = O(n)
        # Space Complexity = O()
        new_node = Node(new_data)
        curr_node = self.head
        prev_node = self.head
        if self.head is None:
            self.head = new_node
        else:
            while curr_node:
                if curr_node.next is None:
                    curr_node.next = new_node
                    break
                curr_node = curr_node.next

    # Function to get the middle of
    # the linked list
    def printMiddle(self):
        # Time Complexity = O(n)
        # Space Complexity = O(1)
        curr_node = self.head
        length = 0
        while curr_node:
            length += 1
            curr_node = curr_node.next

        curr_node = self.head
        target = (length + 1) // 2
        counter = 0
        while curr_node:
            counter += 1
            if counter == target:
                print(curr_node.data)
                return
            curr_node = curr_node.next


# Driver code
list1 = LinkedList()
list1.push(5)
list1.push(4)
list1.push(2)
list1.push(3)
list1.push(1)
list1.printMiddle() 
