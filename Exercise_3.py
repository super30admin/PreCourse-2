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
        if self.head is None:
            self.head = Node(new_data)
        else:
            node = self.head
            while node.next is not None:
                node = node.next
            node.next = Node(new_data)

    # Function to get the middle of
    # the linked list

    def getMiddle(self):

        slow, fast = self.head, self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def printMiddle(self):
        node = self.getMiddle()
        while node is not None:
            print(node.data)
            node = node.next

if __name__ == "__main__":
    # Driver code
    list1 = LinkedList()
    list1.push(5)
    list1.push(4)
    list1.push(3)
    list1.push(2)
    list1.push(1)
    list1.printMiddle()