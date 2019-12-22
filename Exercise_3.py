class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def push(self,new_data):
        if self.head is None:
            newnode=Node(new_data)
            self.head=newnode
        else:
            current=self.head
            while(current.next!=None):
                current=current.next
            current.next=Node(new_data)
            
    def print(self):
        temp=self.head
        while(temp):
            print(temp.data,end='')
            temp=temp.next

    def middle(self):
        slow_ptr=self.head
        fast_ptr=self.head
        while(fast_ptr.next.next!=None and fast_ptr.next!=None):
            slow_ptr=slow_ptr.next
            fast_ptr=fast_ptr.next.next
        if fast_ptr.next != None:
            slow_ptr = slow_ptr.next
        return slow_ptr.data
            
            
if __name__=="__main__":
    list1=LinkedList()
    list1.push(5)
    list1.push(4)
    list1.push(2)
    list1.push(3)
    list1.push(1)
    list1.push(6)
    list1.print()
    print()
    print(list1.middle())
    
