// Time Complexity : O(n)
// Space Complexity : O(1)
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : No

class LinkedList_1 
{ 
    Node head; // head of linked list 
  
    /* Linked list node */
    class Node 
    { 
        int data; 
        Node next; 
        Node(int d) 
        { 
            data = d; 
            next = null; 
        } 
    } 
  
 
    void printMiddle() 
    { 
        Node slow_pointer = head;
        Node fast_pointer = head;
        int check = 0;
        while(fast_pointer != null && slow_pointer != null){
            if(fast_pointer.next == null ){
                check = 1;
                break;
            }
            else if(fast_pointer.next.next == null){
                check = 2;
                break;
            }
            slow_pointer = slow_pointer.next;
            fast_pointer = fast_pointer.next.next;
        }
        if(check == 1){
            System.out.println(slow_pointer.data);
        }
        if(check == 2){
            System.out.println(slow_pointer.next.data);
        }
        
    } 
  
    public void push(int new_data) 
    { 
        Node new_node = new Node(new_data); 
        new_node.next = head; 
        head = new_node; 
    } 

    public void printList() 
    { 
        Node tnode = head; 
        while (tnode != null) 
        { 
            System.out.print(tnode.data+"->"); 
            tnode = tnode.next; 
        } 
        System.out.println("NULL"); 
    } 
  
    public static void main(String [] args) 
    { 
        LinkedList_1 llist = new LinkedList_1(); 
        for (int i=15; i>0; --i) 
        { 
            llist.push(i); 
            llist.printList(); 
            llist.printMiddle(); 
        } 
    } 
} 