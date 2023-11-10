#time complexity : O(n)
#space complexity : O(1)

# Node class
class ListNode:

    # Function to initialise the node object
    def __init__(self, data, next=None):
        self.data=data
        self.next=None


class LinkedList:

    def __init__(self):
        self.head=None

    def push(self, new_data):
        if (self.head == None):

            self.head = ListNode(new_data)


        else:
            tmp = self.head

            while (tmp.next != None):

                tmp = tmp.next
            newnode = ListNode(new_data)

            tmp.next = newnode


    # Function to get the middle of
    # the linked list
    def printMiddle(self):
        fp=self.head
        sp=self.head
        while(fp!=None and fp.next!=None):
            sp=sp.next
            fp=fp.next.next
        print(sp.data)

# Driver code
list1 = LinkedList()
list1.push(5)
list1.push(4)
list1.push(2)
list1.push(3)
list1.push(1)
list1.push(8)
list1.printMiddle()
