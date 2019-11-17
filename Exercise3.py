class Node:
    # Function to initialise the node object
    def __init__(self, data):
        self.data = data
        self.nextNode = None

class LinkedList:
    def __init__(self):
        self.headval = None

    def push(self, new_data):
        if self.headval is None:
            self.headval = Node(new_data)
        a = self.headval
        while(a.nextNode):
            a = a.nextNode
        a.nextNode = Node(new_data)

    # Function to get the middle of the linked list
    def printMiddle_with_list(self):
        # saving all node values in list and returning mid point of list
        array = []
        # variable to save length of array instead of performing len(array) at end
        i = 0
        a = self.headval
        # Iterating through linked list to save node values to list
        while a.nextNode is not None:
            a = a.nextNode
            i +=1
            array.append(a.data)
        if (i%2==0):
            print("Middle nodes of linked list (using list) is : ",array[int((i/2)-1)])
        else:
            print("Middle node of linked list (using list) is: ",array[int(i/2)])

    def printMiddle_with_pointers(self):
        slow = fast = self.headval
        while (fast is not None) and (fast.nextNode is not None):
            slow = slow.nextNode
            fast = fast.nextNode.nextNode
        print("Middle node of linked list (using two pointers) is: ",slow.data)

# Driver code
list1 = LinkedList()
list1.push(6)
list1.push(5)
list1.push(4)
list1.push(3)
list1.push(2)
list1.push(1)
list1.printMiddle_with_list()
list1.printMiddle_with_pointers()

'''
#output

Middle nodes of linked list (using list) is :  4
Middle node of linked list (using two pointers) is:  4
'''
