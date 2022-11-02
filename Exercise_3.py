"""
	Problem Statement: Implement a linked list.

	Time Complexity: 
	push(): O(1) if linked list is empty else O(n)
	print_list(): O(1) if linked list is empty else O(n)
	print_middle(): O(n / 2) -> Ignoring the cooefficient 1/2, hence O(n)

    Space Complexity:
    Auxiliary Space: O(n)

"""


class Node:
    def __init__(self, data):  
        self.data = data
        self.next = None

class LinkedList: 
    def __init__(self): 
        self.length = 0
        self.head = None
  
    def push(self, new_data):
        if self.head == None:
            self.head = Node(new_data)
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = Node(new_data)
        self.length += 1

    def print_list(self):
        temp = self.head
        while temp:
            print(f"{temp.data} {'-> ' if temp.next else ''} ", end="" if temp.next else "\n")
            temp = temp.next

    def print_middle(self):
        if self.length > 0:
            mid = self.length // 2
            temp = self.head

            while mid > 0:
                temp = temp.next
                mid -= 1
            print(f"Middle element in linked list is {temp.data}.")
        else:
            print(f"Linked list is empty.")

if __name__ == '__main__':
    list = LinkedList() 

    list.push(5)
    list.push(4)
    list.push(2)
    list.push(34)
    list.push(2234)
    list.push(232)
    list.push(223434)
    list.push(3234)
    list.push(32343)
    list.push(1)
    list.print_list()
    list.print_middle()