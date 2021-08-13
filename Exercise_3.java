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
    //Time complexity o(n)
    //Space complexity o(1)
    void printMiddle() 
    { 
        //Write your code here
	//Implement using Fast and slow pointers
        Node p1=head,p2=head;
        while(p2!=null&&p2.next!=null){
            p1=p1.next;
            p2=p2.next.next;
        }
        System.out.println(p1.data);
    }
    //Time complexity o(1)
    //Space complexity o(1)
    public void push(int new_data) 
    { 
        Node new_node = new Node(new_data); 
        new_node.next = head; 
        head = new_node; 
    }
    //Time complexity o(n)
    //Space complexity o(1)
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