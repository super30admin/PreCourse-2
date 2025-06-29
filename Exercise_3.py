'''
Find Mid Point of a Singly Linked List.
'''

# Time Complexity : O(n) where n is the number of nodes in the linked list. 
# Space Complexity : O(1) as we are using only a constant amount of space for pointers and counters.
# Did this code successfully run on Leetcode : Yes, the code runs successfully on GeeksforGeeks.
# Any problem you faced while coding this : Yes, I faced some issues with understanding how to traverse the linked list and find the middle element efficiently. However, after some research and practice, I was able to implement the solution correctly.

# Node class  
class Node:  # humne Node class banaya hai jo linked list ke har node ko represent karega. (We have created a Node class that will represent each node in the linked list.)
    # Function to initialise the node object  
    def __init__(self, data): # humne Node class ka constructor banaya hai jo data aur next pointer ko initialise karega. (We have created a constructor for the Node class that will initialize the data and next pointer.)
        self.data = data # yeh data ko self.data mein store karega. (This will store the data in self.data.)
        self.next = None # yeh next pointer ko None se initialise karega. (This will initialize the next pointer to None.)
        
class LinkedList: # humne LinkedList class banayi hai jo linked list ko represent karegi. (We have created a LinkedList class that will represent the linked list.)

    def __init__(self): # humne LinkedList class ka constructor banaya hai jo head aur count ko initialise karega. (We have created a constructor for the LinkedList class that will initialize the head and count.)
        self.head = None # yeh head ko None se initialise karega. (This will initialize the head to None.)
        self.count = 0 # yeh count ko 0 se initialise karega. (This will initialize the count to 0.)    

    def push(self, new_data): # humne push function banaya hai jo linked list mein naye node ko add karega. (We have created a push function that will add a new node to the linked list.)
        new_node = Node(new_data) # yeh Node class ka ek naya instance new_node banayega. (This will create a new instance of the Node class called new_node.)
        new_node.next = self.head # yeh new_node ke next pointer ko current head se point karega. (This will point the new_node's next pointer to the current head.)
        self.head = new_node # yeh current head ko new_node ki taraf point karega. (This will point the current head to the new_node.)
        self.count += 1 # yeh count ko 1 se increment karega. (This will increment the count by 1.)

    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): # humne printMiddle function banaya hai jo linked list ka middle element print karega. (We have created a printMiddle function that will print the middle element of the linked list.)
        if self.head is None: # agar head None hai, toh linked list khali hai. (If the head is None, then the linked list is empty.)
            print("The linked list is empty, no middle element.")  # print karega. (This will print a message indicating that the linked list is empty and there is no middle element.)
            return None # None return karega. (This will return None.)
        '''
        Here we used Tortoise and Hare algorithm to find the middle element.
        The slow pointer moves one step at a time, while the fast pointer moves two steps at a time.
        When the fast pointer reaches the end of the list, the slow pointer will be at the middle element.
        # Dry Run:
        Input: 1 -> 2 -> 3 -> 4 -> 5
        Output: The middle element is: 3
        Initially, both slow and fast pointers point to the head of the list i.e. at 1.
        In the first iteration, slow moves to 2 and fast moves to 3.
        In the second iteration, slow moves to 3 and fast moves to 5.
        In the third iteration, slow moves to 4 and fast reaches the end of the list.
        Now, slow is at the middle element which is 3.
        This algorithm runs in O(n) time complexity and O(1) space complexity.
        '''
        slow = fast = self.head # humne slow aur fast pointers ko head se initialise kiya hai. (We have initialized both slow and fast pointers to the head of the linked list.)
        # Traverse the linked list with slow moving one step and fast moving two steps
        while fast is not None and fast.next is not None: # jab tak fast pointer None nahi hai aur fast ka next pointer bhi None nahi hai, tab tak loop chalega. (This loop will run until the fast pointer is not None and the fast's next pointer is also not None.)
            slow = slow.next # slow pointer ko ek step aage badhaenge. (We will move the slow pointer one step forward.)
            fast = fast.next.next # fast pointer ko do steps aage badhaenge. (We will move the fast pointer two steps forward.)
        # When fast pointer reaches the end, slow pointer will be at the middle element
        # jab fast pointer end tak pahunchta hai, toh slow pointer middle element par hoga. (When the fast pointer reaches the end, the slow pointer will be at the middle element
        print("The middle element is:", slow.data) # middle element print karega. (This will print the middle element.)
        return slow.data # middle element return karega. (This will return the middle element.)

# Driver code
llist = LinkedList()
llist.push(5)
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)
llist.printMiddle()

# Dry Run
# Input: 1 -> 2 -> 3 -> 4 -> 5
# Output: The middle element is: 3

