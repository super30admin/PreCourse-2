// Time Complexity : printMiddle:O(n)
// Space Complexity :O(1)
// Did this code successfully run on Leetcode :yes
// Any problem you faced while coding this : no


// Your code here along with comments explaining your approach

// Assigned tow points one for increments one spot and other increments two spots at a time and checked if the fastpointer reaches the end of list with null checks and returned the slowpointer as the middle element.



class Exercise_3 
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
    Node slowPtr=head;
    Node fastPtr=head;
    while(fastPtr!=null && fastPtr.next!=null){
        slowPtr=slowPtr.next;
        fastPtr=fastPtr.next.next;
    }
    System.out.println(slowPtr.data);
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
        Exercise_3 llist = new Exercise_3(); 
        for (int i=15; i>0; --i) 
        { 
            llist.push(i); 
            llist.printList(); 
            llist.printMiddle(); 
        } 
    } 
} 