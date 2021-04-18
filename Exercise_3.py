# Node class
class Node:
    __slots__ = 'data', 'link'

    # Function to initialise the node object  
    def __init__(self, data, link=None):
        self.data = data
        self.link = link

    def __str__(self):
        """ Return a string representation of the contents of
            this node. The link is not included.
        """
        return str(self.data)


class LinkedList:
    __slots__ = 'head'

    def __init__(self):
        self.head = None

    # def traverse_list(self):
    #     if self.head is None:
    #         print("List has no elements")
    #         return
    #     else:
    #         n = self.head
    #         while n is not None:
    #             print(n.data, " ")
    #             n = n.link

    def push(self, new_data):
        new_node = Node(new_data)
        nodes.append(new_node)
        if LinkedList.isEmpty(self):
            self.head = new_node
            return
        else:
            current = self.head
            while current.link is not None:
                current = current.link
            current.link = new_node

    def isEmpty(self):
        return self.head is None

    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        if self.head is None:
            print("List has no elements")
            return
        else:
            count = 1
            current = self.head
            while current.link is not None:
                count = count + 1
                current = current.link

        mid = count//2
        print(str(nodes[mid]))


# Driver code
nodes = []
list1 = LinkedList()
list1.push(5)
list1.push(4)
list1.push(2)
list1.push(3)
list1.push(1)
list1.printMiddle()
