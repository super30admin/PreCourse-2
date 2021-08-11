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
        if not self.head:
            self.head = Node(new_data)
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = Node(new_data)

    # def display(self):
    #     """
    #     Debugging func to display contents
    #     """
    #     ans = []
    #     temp = self.head
    #     while temp:
    #         ans.append(temp.data)
    #         temp = temp.next
    #     print(ans)
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        # two pointer runner technique
        # first, second pointer, first inc by 1, second inc by 2
        # of course, assuming the linked list has an odd number of elements
        first, second = self.head, self.head
        while second.next:
            print((first.data, second.data))
            second = second.next.next
            first = first.next
            if not second:
                break
        print(first.data)

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
# list1.push(22)
# list1.display()
list1.printMiddle() 
