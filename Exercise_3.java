// Time Complexity : O(n) (n - number of nodes)
// Space Complexity : O(1) (space used by fast and slow)
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : N/A
class LinkedList1 
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
        Node slow = head;
        Node fast = head;
        
        while(fast!=null && fast.next!=null)
        {
            slow = slow.next;
            fast = fast.next.next;
        }
        System.out.println("Mid Point of the above Singly Linked List is: ");
        while(slow!=null)
        {
            System.out.print(slow.data+"->");
            slow=slow.next;
        }
        System.out.println("NULL");   
    } 
  
    public void push(int new_data) 
    { 
        Node new_node = new Node(new_data); 
        new_node.next = head; 
        head = new_node; 
    } 

    public void printList() 
    { 
        System.out.println(); 
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
        LinkedList1 llist = new LinkedList1(); 
        for (int i=15; i>0; --i) 
        { 
            llist.push(i); 
            llist.printList(); 
            llist.printMiddle(); 
        } 
    } 
} 