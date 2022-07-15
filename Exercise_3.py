'''2 Approaches'''
'''
Algorithm (Fylod's Algorithm aka Tortoise and Hare Algorithm)
    printMiddle(arr, low, high):
        1. If there are no elements in the linked list return None
        2. Initialize first and second pointer to head
        3. If second and secnd.next are not None continue as go to step 6
        4. For second take 2 steps by setting it to second.next.next
        5. For first take 1 steps by setting it to first.next. Thus the second pointer
           will moveat twice the speed of first one. So if it reaches the end of the list 
           first will be at the middle of the list
        6. Print first.data

LinkedList
    Space Complexity: space complexity of the node * no of elements in linked list = O(2) * O(n) = O(2n) = O(n)
    push(new_data):
        Time Complexity: O(1) as we simply need to append new node to next of self.curr
    
    printMiddle(arr):    
        Time Complexity: O(n / 2) = O(n) as we are travesing the list at twice the speed
'''
# Node class


class Node:

    # Function to initialise the node object
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:

    def __init__(self):
        self.head = None
        self.curr = None

    def push(self, new_data):
        if not self.head:
            self.head = Node(new_data)
            self.curr = self.head
            return True
        self.curr.next = Node(new_data)
        self.curr = self.curr.next
        return True
    # Function to get the middle of
    # the linked list

    def printMiddle(self):
        if not self.head:
            print(None)
            return None
        first = second = self.head
        while second and second.next != None:
            first = first.next
            second = second.next.next
        print(first.data)
        return first.data


# Driver code
list1 = LinkedList()
list1.push(5)
list1.push(4)
list1.push(2)
list1.push(3)
list1.push(1)
list1.printMiddle()

# ######################Additional Test Cases##########################
# (1) Empty List
list1 = LinkedList()
op = list1.printMiddle()
assert op == None, f"Expected None as output but instead got {op }"

# (2) Single Element List
list1 = LinkedList()
list1.push(5)
op = list1.printMiddle()
assert op == 5, f"Expected 5 as output but instead got {op }"

# (2) Even small List
list1 = LinkedList()
list1.push(4)
list1.push(5)
op = list1.printMiddle()
assert op == 5, f"Expected 5 as output but instead got {op }"

# (2) Odd Small List
list1 = LinkedList()
list1.push(4)
list1.push(5)
list1.push(3)
op = list1.printMiddle()
assert op == 5, f"Expected 5 as output but instead got {5}"

# (2) Even long List
list1 = LinkedList()
list1.push(1)
list1.push(2)
list1.push(3)
list1.push(4)
list1.push(5)
list1.push(6)
op = list1.printMiddle()
assert op == 4, f"Expected 4 as output but instead got {op }"

# (2) Odd long List
list1 = LinkedList()
list1.push(1)
list1.push(2)
list1.push(3)
list1.push(4)
list1.push(5)
list1.push(6)
list1.push(7)
op = list1.printMiddle()
assert op == 4, f"Expected 4 as output but instead got {4}"

########################################################################
'''
Algorithm 

    1. Initiate self.mid to self.head
    2. Set self.mid to self.mid.next if self.length is an odd value
    3. To print mid simply use self.mid.data

LinkedList
    Space Complexity: space complexity of the node * no of elements in linked list = O(2) * O(n) = O(2n) = O(n)
    push(new_data):
        Time Complexity: O(1) as we simply need to append new node to next of self.curr
    
    printMiddle(arr):    
        Time Complexity: O(1) as we are storing the mid value during push
'''
# Node class
print(f"Find mid a linked list")


class Node:

    # Function to initialise the node object
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:

    def __init__(self):
        self.head = None
        self.curr = None
        self.length = 0
        self.mid = None

    def push(self, new_data):
        if not self.head:
            self.head = Node(new_data)
            self.curr = self.head
            self.mid = self.head
            self.length += 1
            return True
        self.curr.next = Node(new_data)
        self.curr = self.curr.next

        if self.length % 2 != 0:
            self.mid = self.mid.next
        self.length += 1
        return True
    # Function to get the middle of
    # the linked list

    def printMiddle(self):
        if not self.mid:
            print("None")
            return None
        print(self.mid.data)
        return self.mid.data


# Driver code
list1 = LinkedList()
list1.push(5)
list1.push(4)
list1.push(2)
list1.push(3)
list1.push(1)
list1.printMiddle()
# ######################Additional Test Cases##########################
# (1) Empty List
list1 = LinkedList()
op = list1.printMiddle()
assert op == None, f"Expected None as output but instead got {op }"

# (2) Single Element List
list1 = LinkedList()
list1.push(5)
op = list1.printMiddle()
assert op == 5, f"Expected 5 as output but instead got {op }"

# (2) Even small List
list1 = LinkedList()
list1.push(4)
list1.push(5)
op = list1.printMiddle()
assert op == 5, f"Expected 5 as output but instead got {op }"

# (2) Odd Small List
list1 = LinkedList()
list1.push(4)
list1.push(5)
list1.push(3)
op = list1.printMiddle()
assert op == 5, f"Expected 5 as output but instead got {5}"

# (2) Even long List
list1 = LinkedList()
list1.push(1)
list1.push(2)
list1.push(3)
list1.push(4)
list1.push(5)
list1.push(6)
op = list1.printMiddle()
assert op == 4, f"Expected 4 as output but instead got {op }"

# (2) Odd long List
list1 = LinkedList()
list1.push(1)
list1.push(2)
list1.push(3)
list1.push(4)
list1.push(5)
list1.push(6)
list1.push(7)
op = list1.printMiddle()
assert op == 4, f"Expected 4 as output but instead got {4}"

########################################################################
