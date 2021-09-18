# Time Complexity = O(n)
# Space Complexity = O(n)

# Node class
class Node:

    # Function to initialise the node object
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self): # initializing linkedlist object
        self.head = None

    def push(self, new_data): # code to create new node at front of linkedlist

        newnode = Node(new_data)
        newnode.next = self.head
        self.head = newnode

    # Function to get the middle of the linked list - Using 2 ptr approach
    def printMiddle(self):
        firstptr = self.head
        secondptr = self.head

        if self.head is not None: # start only if linked list is not empty

            while(secondptr.next is not None and secondptr.next.next is not None): # loop until secondptr reaches end of linkedlist
                secondptr = secondptr.next.next
                firstptr = firstptr.next
            print("Middle Element =  ",firstptr.data) # when secondptr reaches end, firstptr has to point to middle of linkedlist - because logic is
            # travel distance of first ptr = exactly 1/2 * travel distance of second ptr



# Driver code
list1 = LinkedList()
list1.push(5)
list1.push(4)
list1.push(2)
list1.push(3)
list1.push(1)
list1.printMiddle() 
