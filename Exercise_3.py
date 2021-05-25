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
        node = Node(new_data)
        node.next = self.head
        self.head = node

  
    # Function to get the middle of  
    # the linked list
# TODO:
#     Time Complexity = Big O(N)
#     Space Complexity = Big O(1)

    def printMiddle(self):
        jump_by_1 = self.head
        jump_by_2 = self.head

        while (jump_by_2.next and jump_by_2):
            jump_by_1 = jump_by_1.next
            jump_by_2 = jump_by_2.next.next
        print("Mid value", jump_by_1.data)

if __name__ == '__main__':
# Driver code 
    list1 = LinkedList()
    list1.push(5)
    list1.push(4)
    list1.push(2)
    list1.push(3)
    list1.push(1)
    list1.printMiddle()
