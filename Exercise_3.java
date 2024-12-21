// Time Complexity : Need to refresh my knowledge on this.
// Space Complexity : Need to refresh my knowledge on this.
// Did this code successfully run on Leetcode : YES(Over local ide).
// Any problem you faced while coding this : None, other than t.c and s.c.
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
        Node slowPointer = head;
        Node fastPointer = head;
        //loop until the fastPointer hasn't reached the point where it can't move further.
        while(fastPointer != null && fastPointer.next != null){
            slowPointer = slowPointer.next; //slow one moves 1 step at a time.
            fastPointer = fastPointer.next.next;// fast one moves 2 step at a time.
        }

        System.out.println("Middle element :" + slowPointer.data);
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