// Time Complexity :
//   printMiddle() -> O(n)
//   push()        -> O(1)
//   printList()   -> O(n)
// Space Complexity : O(1) extra space (we only use a few pointers)
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this :
//   - Must handle the empty-list case to avoid NullPointerException.
//   - With fast/slow pointers on even-length lists, this prints the *second* middle (common convention).
// Your code here along with comments explaining your approach
//   - Use two pointers: 'fast' moves two nodes at a time and 'slow' moves one.
//   - When 'fast' reaches the end (null) or the node before the end (fast.next == null),
//     'slow' will be at the middle. Then print slow.data.
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
    // Handle empty list
    if (head == null) {
        System.out.println("Middle element: (list is empty)");
        return;
    }

    // Fast and slow pointers
    Node slow = head; 
    Node fast = head; 

    // Move fast by 2 and slow by 1. When fast reaches end, slow is at middle.
    while (fast != null && fast.next != null) {
        slow = slow.next; 
        fast = fast.next.next; 
    }

    System.out.println("Middle element: " + slow.data);

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