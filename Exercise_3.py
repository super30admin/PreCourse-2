# Node class
# This is Singly Linked list
# Time complexity, push operation = O(N), findMiddle = O(N)
# Space complexity, O(N)
# Did it run in leetcode successfully? Yes, and the output of the program is enough for validation.
# did you face any problems? Nothing major!!


class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList: 
  
    def __init__(self): 
        self.head = None
        self.len = 0
  
    def push(self, new_data):
        self.len += 1
        if self.head == None:
            self.head = Node(new_data)

        else:
            def traverse(node):
                # recursively traverse till the end
                if node.next == None:
                    node.next = Node(new_data)
                    return node
                else:
                    node.next = traverse(node.next)
                    return node

            self.head = traverse(self.head)
        
    def show(self):
        a = []

        def traverse(node):
            # recursively traverse till the end
            if node == None:
                return
            else:
                a.append(node.data)
                return traverse(node.next)

        traverse(self.head)
        print(a)
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        # simple approach
        # I am maintaining a self.len variable to store the size of the linkedlist.
        # Getting the middle element will be a straight forward task
        count = 0
        mid_index = (self.len // 2) + 1

        def traverse(node, count):
            # recursively traverse till the middle element
            count += 1
            if count == mid_index:
                return node.data
            return traverse(node.next, count)

        mid_element = traverse(self.head, count)
        print('Middle element is ', mid_element)



# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4)
list1.push(2)
list1.push(3)
list1.push(1)
list1.push(1)
list1.show()
list1.printMiddle() 
