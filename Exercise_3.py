'''
Find the midpoint of a singly-linked list.

Time Complexity:
    push(): O(n) if inserted at the tail as done here, O(1) if pushed at the head
    printMiddle(): O(n/2) ~ O(n) as we traverse half the length of the linked list

Space Complexity:
    push(): O(1) since the size of auxiliary space does not change since we are pusing one element for each single push() call.
            However, O(n) when we consider all n inputs to the linked list itself.
    printMiddle(): O(1)

Issue while implementing: No


'''

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
            #Find the last element of the linked list first
            current = self.head
            while current.next is not None:
                current = current.next

            #Add to the end of the linked list
            current.next = Node(new_data)


    # Function to get the middle of the linked list
    def printMiddle(self):




        if self.head is None:
            return -1
        else:

            # find the length of the linked list first
            curr = self.head
            ctr = 1
            while curr is not None:
                ctr += 1
                curr = curr.next

            # Now we have the length of the linked list, now start from the head and find the element at this index
            curr = self.head
            loc = ctr/2
            curr_loc = 1
            while curr_loc < loc:
                curr = curr.next
                curr_loc += 1

            print(curr.data)



# Driver code 


list1 = LinkedList()
list1.push(5)
list1.push(4)
list1.push(2)
list1.push(3)
list1.push(1)
list1.printMiddle()
