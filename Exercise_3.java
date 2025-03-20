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
        int i = 0;
        Node tNode = head;
        while (i < getLength()/2 && tNode.next != null) {
            i++;
            tNode = tNode.next;
        }

        System.out.printf("Middle element is %d", tNode.data);
        System.out.println("\n");
    } 

    public int getLength() {
        Node tNode = head;
        int len = 0;
        while (tNode != null) {
            tNode = tNode.next;
            len++;
        }

        return len;
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