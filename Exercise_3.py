# Node class
#timecomplexity: O(n), space complexity: O(1)
#no problems face while solving
class Node:

    # Function to initialise the node object  
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def push(self, new_data):
        # if the head doesn't exist create a new node and assign it as head
        if self.head is None:
            self.head = Node(data)
        # else Create a new node and point it towards head and reassign the new node as head
        else:
            newnode = Node(data);
            newnode.next = self.head
            self.head = newnode

    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        # base conditions
        if self.head is None:
            return print(None)
        if self.head.next is None:
            print(self.head.data)
        else:
            iter1 = iter2 = self.head
            #iterate through 2 types of iterators, with one iterating twice as fast
            while iter2 and iter2.next is not None:
                iter1 = iter1.next
                iter2 = iter2.next.next
            print(iter1.data)


# Driver code 
list1 = LinkedList()
list1.push(5)
list1.push(4)
list1.push(2)
list1.push(3)
list1.push(1)
list1.printMiddle()
