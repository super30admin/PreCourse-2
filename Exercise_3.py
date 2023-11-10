# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data): 
        self.data=data
        self.next=None 
        
class LinkedList: 
  
    def __init__(self): 
        
  
     def push(self, new_data,head1): 
        new_node=Node(new_data)
        new_node.next=head1
        head1=new_node
        return head1



        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self,head): 
        if head!=None:
            len=self.getLen(head)
            temp=head

            mid=len//2
            while mid!=0:
                temp.next
                mid-=1
            print('middle element %d' %temp.data)

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 
