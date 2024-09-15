# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data, next):
        self.data = data
        self.next = next
class LinkedList: 
  
    def __init__(self): 
        self.head = None
  
    def push(self, new_data):
        if self.head is None:
            self.head = Node(new_data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(new_data, None)

    def get_length(self):
        itr = self.head
        count = 0
        while itr:
            count += 1
            itr = itr.next
        return count

    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        itr = self.head
        count = self.get_length()
        middle = count // 2
        new_count = 0
        while itr:
            if middle == new_count:
                print(itr.data)
                break
            new_count += 1
            itr = itr.next





# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(12)
list1.push(3)
list1.push(1)
list1.printMiddle() 
