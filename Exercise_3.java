
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : None
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
    Node slow = new Node(-1); // created slow pointer
    Node fast = new Node(-1); // created fast pointer

        slow = head; //slow points to head element
        fast = head; //fast points to head element
    
        while(fast.next!=null) // traversing till fast points to null i.e reaches the end of the list
        {   slow = slow.next; // incrementing slow by one element
            fast = fast.next.next; // incrementing fast by twice the speed of slow
        }

        System.out.println("The Middle element in the list is" + slow.data); // slow pointer points to mid element when fast reaches end as slow was moving at half the speed of fast pointer
        // Time Complexity : O(n)
        // Space Complexity : O(1)

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
    } 
    llist.printList(); 
    llist.printMiddle(); 
        } 
} 