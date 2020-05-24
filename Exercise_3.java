// Time Complexity : O(n) (LinkedList size, fastpointer traverses entire list to reach the end of list)
// Space Complexity : O(n) (Linked List, no extra memory used)
// Did this code successfully run on Leetcode : No, ran in other ide's
// Any problem you faced while coding this :


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
        Node fast = head; // Initialize fast and slow pointer, fast pointer moves 2 positions(nodes) and slow pointer moves 1
	    Node slow = head; // when fast pointer reaches the end of list, slow pointer reaches the middle of list
	    while (fast!= null && fast.next!=null) { // continue till fast reaches the last element
	        fast = fast.next.next; 
	        slow = slow.next; 
	    }
	    System.out.println("Middle Element is : " +slow.data); // print slow pointers data : the middle element

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