'''
====== Submission Details =======
Student Name: Pavan Kumar K. N.
Email       : pavan1011@gmail.com
S30 SlackID : RN32MAY2021
=================================
'''

# Node class  
class Node:  
    # Function to initialise the node object  
    def __init__(self, data, next_node = None): 
        self.data = data # Data module of the linked list node
        self.next_node = next_node # Pointer to next_node node in the linked list

    def __str__(self):
        str_repr = ""
        str_repr = f"[{self.data}]->"

        if self.next_node is not None:
            str_repr += self.next_node.__str__()
        else:
            str_repr += "NULL"

        return str_repr
        
class LinkedList: 

    def __init__(self): 
        self.head = None
        
    def push(self, new_data):
        print(f"Pushing data: {new_data}")
        new_node = Node(new_data)

        print(f"    Created new node: {new_node}")
        new_node.next_node = self.head
        print(f"    new node: {new_node}")

        self.head = new_node
        print(f"    Pushed node. Head is now:{self.head}")

    # def printList(self):
    #     last = self.head
    #     while last is not None:
    #         print(f"{last.data}->", end="")
    #         last = last.next_node
    #         if(last is None):
    #             print("NULL")  
    
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        print(f"Head: {self.head}")
        print("Middle: ", end="")
        last = self.head
        mid = self.head
        count = 0
        while last is not None:
            if count&1 == 1:
                mid = mid.next_node
            last = last.next_node
            count+=1

        print(mid)

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
# list1.push(1)
# list1.printList()

list1.printMiddle() 
