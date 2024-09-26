// Time Complexity : O(N/2)
// Space Complexity : O(1)
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : Learned the concept of fast pointer and slow pointer


// Your code here along with comments explaining your approach
//Find Mid Point of a Singly Linked List.

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
        Node fast_pointer = head;
        Node slow_pointer = head;

        if(head != null){
            while(fast_pointer != null && fast_pointer.next !=null){
                fast_pointer = fast_pointer.next.next;
                slow_pointer = slow_pointer.next;
            }
            System.out.println("Middle Element - " + slow_pointer.data);
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
        Exercise_3 llist = new Exercise_3(); 
        for (int i=15; i>0; --i) 
        { 
            llist.push(i); 
            llist.printList(); 
            llist.printMiddle(); 
        } 
    } 
} 