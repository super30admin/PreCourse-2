// Time Complexity : O(n)
// Space Complexity : O(1)
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : no
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

        // no middle element if there isnt any node
        if(head==null) return;

        // head is the middle element if there is only one element
        if(head.next==null) {
            System.out.println(head.data);
            return;
        }

        Node slow = head;
        Node fast = head;

        // forward the slow pointer by 1 and fast pointer by 2 by checking the fact that fast pointer is not null and the next element to fast is not null
        while(fast!=null && fast.next!=null) {
            fast = fast.next.next;
            slow = slow.next;
        }

        // print out the slow pointer which points to the second element if there are two mid elements and mid pointer if there is one
        System.out.println(slow.data);
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