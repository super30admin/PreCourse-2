class LinkedList 
{ 
    Node head; // head of linked list 

    // Time Complexity :
    // Space Complexity :
    // Did this code successfully run on Leetcode :
    // Any problem you faced while coding this :
    /* Linked list node */
    class Node 
    { 
        int data; 
        Node next; 
        Node(){}
        Node(int d) 
        { 
            data = d; 
            next = null; 
        } 
    } 
    LinkedList(){
        this.head = null;
    }
    /* Function to print middle of linked list */
   //Complete this function
    void printMiddle() { 
        //Write your code here
	//Implement using Fast and slow pointers
        // edge cases single node 
        if(head == null) System.out.println("Empty List");
        else if( head.next == null) System.out.println(head.data);
        /* edge cases two nodes - 
            dont thik there will be any middle nodes for even nodes */
        
        else {// three nodes or node 
            Node fast = new Node();
            Node slow = new Node();
            fast.next = head;
            slow = fast;
            while(fast!= null && fast.next != null ){
                fast = fast.next.next;
                if(fast == null) { System.out.println(slow.next.data);}
                slow = slow.next;
            }
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
        LinkedList llist = new LinkedList(); 
        for (int i=1; i<16; i++) 
        { 
            llist.push(i); 
            llist.printList(); 
            llist.printMiddle(); 
        } 
    } 
} 