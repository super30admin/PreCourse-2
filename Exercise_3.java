/*
Time Complexity : O(n) since traversing the entire arraylist.
Space Complexity : O(n) since we create memory when linked list is generated

Did this code successfully run on Leetcode :
Finished in 81 ms
1->2->3->4->5->6->7->8->9->10->11->12->13->14->15->NULL
Mid of the list is 8

Any problem you faced while coding this :
Renamed the class due to Leetcode giving compiling issues due to Conflict with java.util.LinkedList class.

Your code here along with comments explaining your approach :
Straight forward approach for two pointers.
*/
class MyLinkedList 
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
	    //Implement using Fast and slow pointers
        Node slowPointer = head;
        Node fastPointer = head;
         
        while (fastPointer != null && fastPointer.next != null){
            slowPointer = slowPointer.next;
            fastPointer = fastPointer.next.next;
        }
        System.out.println("Mid of the list is " + slowPointer.data);
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
        MyLinkedList llist = new MyLinkedList(); 
        for (int i=15; i>0; --i) 
        { 
            llist.push(i); 
        }
        llist.printList(); 
        llist.printMiddle(); 
    } 
} 