// Time Complexity : O(n)
// Space Complexity : O(1) Not sure If it is O(n) 
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : No


// Your code here along with comments explaining your approach
/*
 * Used Fast and Slow pointer
 * Used while loop and shifted slow pointer by one position and 
 * fast pointer by two position till Fast pinter is null OR
 * fast pointer.next is null
 * So now slow pointer is in middle 
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
        Node slow = this.head;
        Node fast = this.head;

        while(fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        Node temp = this.head;
        this.head = slow;
        printList("Mid-List");
        this.head = temp;

    } 
  
    public void push(int new_data) 
    { 
        Node new_node = new Node(new_data); 
        new_node.next = head; 
        head = new_node; 
    } 

    public void printList(String msg) 
    { 
        Node tnode = head;
        System.out.print((null == msg ? "Full List: " : msg + ": " )); 
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
            llist.printList(null); 
            llist.printMiddle(); 
        } 
    } 
} 