// Time Complexity :push - O(1), pop - O(1), printmiddle - O(n)
// Space Complexity : O(n)
// Any problem you faced while coding this : Trying to determine the space nad time complexity of this
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
        //Both the pointers point to the head of the list
        Node slowPtr=head;
        Node fastPtr = head;
        //Iterate until the fast pointer doesn't reach the last node wherein either fastPtr=null or fastPtr.next=null 
        while(fastPtr!=null && fastPtr.next!=null){
            /*For every 2 nodes fast ptr traverses, the slow pointer only traverses once, 
             * therefore, by the time the fast pointer reaches the last node,
             * the slow pointer would have only reached half of the nodes
             */
            //Just moves to the next node
            slowPtr = slowPtr.next;
            //fast ptr moves to the next node of the next node
            fastPtr = fastPtr.next.next;
        }
        System.out.println("Middle element is "+slowPtr.data);
    } 
  
    public void push(int new_data)  
    { 
        //Create a new node
        Node new_node = new Node(new_data); 
        //Let the next of this node point to the head node
        new_node.next = head; 
        //assign head to point to this node
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