// Time Complexity : O(n)
// Space Complexity :   O(1) just using pointers
// Did this code successfully run on Leetcode : yes
// Any problem you faced while coding this : no
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
        //Write your code here
	    //Implement using Fast and slow pointers

        Node hare, tortoise;        
        hare = tortoise = head;

        while(hare != null && hare.next != null) {  //loop shall end only when fast pointer ( hare ) reaches null or its next node is null)
            hare = hare.next.next;
            tortoise = tortoise.next;
        }

        System.out.println("The middle element is [" + tortoise.data + "] \n");

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