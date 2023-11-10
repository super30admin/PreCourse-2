// Time Complexity : O(N)
// Space Complexity : O(1)
// Did this code successfully run on Leetcode : ran it successfully on local machine
/* Any problem you faced while coding this : found a bit tricky to maintain the head node and also had tried doing it without fast and slow pointer 
concept.*/

/*
Simple trick concept use 2 variables namely fast and slow. Make the fast variable take two steps at a time while the slow one takes one.
Hence when the fast variable eaches the end of the array the slower one reaches the middle of the array.
*/ 
// Your code here along with comments explaining your approach
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
        Node fast = head;
        Node slow = head;
        /*VERY IMP -- we cannot do fast.next!=null && fast!=null it fails due to short circuit concept of 
        '&&' operator. Here the second condition gets evaluated only when the first one is true. Hence to 
        prevent calling function 'next' on a null value and thereby throwing an Null pointer exception we 
        need to maintain the ordering */

        /*fast!=null && fast.next!=null && fast.next.next!=null this condition nmay be used if we want
         to give 3 instead of 4 as answer in case of even length. */
        if(head!=null){
            while(fast!=null && fast.next!=null){ 
                fast = fast.next.next;

                slow = slow.next;
            }
            System.out.println(slow.data);
        }else{
            System.out.println("NULL");
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
        for (int i=6; i>0; --i) 
        { 
            llist.push(i); 
            llist.printList(); 
            llist.printMiddle();  
        }

    } 
} 