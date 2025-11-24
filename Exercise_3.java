// Time Complexity : O(n)
// Space Complexity : O(1)
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this :
// No major issues. The main challenge was remembering that the fast pointer
// moves two steps at a time while the slow pointer moves one step. This ensures
// the slow pointer reaches the middle when fast reaches the end.


// I used the two-pointer (slow and fast) technique. The fast pointer moves
// two nodes at a time, while the slow pointer moves one node at a time.
// When the fast pointer reaches the end of the list (or becomes null),
// the slow pointer will be pointing to the middle element of the list.
// This approach allows us to find the middle in a single traversal.
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
      if (head == null){
	    System.out.println("The last is empty");
	  return;}
      Node slow = head;
      Node fast = head;
	  while (fast != null && fast.next != null){
		  fast = fast.next.next;
		  slow = slow.next;//Write your code here
	//Implement using Fast and slow pointers
    } 
 	System.out.println("Middle element is: " + slow.data);
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
