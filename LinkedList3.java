// Time Complexity : O(n)
// Space Complexity :O(1)
// Did this code successfully run on Leetcode : -
// Any problem you faced while coding this : -

/*
Implementation of Binary search algorithm to search index of given target element
 */
class LinkedList3
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
   //Fast and slow pointers race, fast goes 2 steps when slow goes 1 step. By the time fast finishes, slow is at middle
    void printMiddle() 
    { 
        Node fast = head;
        Node slow = head;
        while(fast.next!= null && fast.next.next!= null){
            fast = fast.next.next;
            slow = slow.next;
        }
        System.out.println("Middle element is:: " + slow.data);
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
        LinkedList3 llist = new LinkedList3();
        for (int i=15; i>0; --i) {
            llist.push(i);
        }
            llist.printList(); 
            llist.printMiddle();
    } 
} 