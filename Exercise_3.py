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
        push_node = Node(new_data)
        if self.head is None:
            self.head = push_node
            return 

        current = self.head

        while current.next:
            current = current.next

        current.next = push_node # keeping in the end
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        # simple logic we want to find middle of linked list 
        # we can't do like other cases like len(datasturcture)/2 to find the mid, because to find the len of the linked list we need to parse the whole
        # linked list and its complexity will be o(n)
        # but is there a way to not to parse n times but find the mid
        # yes, simple logic so we need to find mid, lets keep a variable to move 1step and one more variable 2 steps 
        # when the second variable reached the end the first variable will be at mid, 2x = len, x = mid 
        # simple logic 
        # edge case we have to handle when the liked list length if even and odd 
        # so in even case if fast is none then we found the mid, odd case if fast.next is none then we found the mid

        if not self.head:
            return None

        slow = self.head
        fast = self.head

        while fast and fast.next : 
            slow = slow.next # moving one step
            fast = fast.next.next # moving 2 steps 

        return slow.data
    # let the linked list be 0-1-2-3-4 odd length, slow =0, fast= 0 next slow =1, fast = 2, slow = 2, fast = 4 ( no more fast.next) so we found the mid
    # let the linked list be 0-1-2-3-4-5 even length, same as above, slow = 3, fast = None the while loop stops as fast is noen and we get the mid 



# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
print(list1.printMiddle()) 
