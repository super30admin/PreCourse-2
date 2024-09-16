/*
** Time Complexity - O(n/2)
** Space Complexity - O(1)
** Did this code successfully run on Leetcode : Yes
** Any problem you faced while coding this : No
*/

class LinkedList 
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
  
    /* Function to print middle of linked list */
   //Complete this function
    void printMiddle() 
    {
    //Implement using Fast and slow pointers
        Node faster_ptr = head;
        Node slower_ptr = head;

        if(head != null) {
            while(faster_ptr != null && faster_ptr.next != null) {
                //forward the pointer two node ahead and move till the pointer reaches to an end
                //forward the pointer one step ahead and once the faster pointer reaches to an end,
                //mid is found
                faster_ptr = faster_ptr.next.next;
                slower_ptr = slower_ptr.next;
            }
            System.out.println("The middle element is :" + slower_ptr.data);
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
        LinkedList llist = new LinkedList(); 
        for (int i=15; i>0; --i) 
        { 
            llist.push(i); 
            llist.printList(); 
            llist.printMiddle();
        } 
    } 
} 