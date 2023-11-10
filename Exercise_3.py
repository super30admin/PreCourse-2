"""
Time Complexity : O(n*log(n) )
Space Complexity : O(n)
Did this code successfully run on Leetcode : N/A
Any problem you faced while coding this :
"""


class Node:

    # Function to initialise the node object  
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        if self.head == None:
            self.head = new_node

        else:
            temp = self.head
            while True:

                if temp.next is None:
                    temp.next = new_node
                    break
                temp = temp.next

    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        '''
        Find the length of the linkedList and then  iterate till mid(length//2), to find the middle element
        '''
        index = 0
        temp = self.head
        while temp:
            temp = temp.next
            index += 1

        mid = index // 2
        index = 0
        temp = self.head
        while temp:
            if index == mid:
                print(temp.data)
            temp = temp.next
            index += 1


# Driver code 
list1 = LinkedList()
list1.push(5)
list1.push(4)
list1.push(2)
list1.push(3)
list1.push(1)
list1.printMiddle() 