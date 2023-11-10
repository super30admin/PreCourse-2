
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
    void printMiddle() 
    { 
        Node i=head;//slow pointer
        Node j=head;//fast pointer
        if (j.next==null || j.next.next==null){
            System.out.println(i.data);
        }
        else{
            while(j.next!=null && j.next.next!=null) {
                i=i.next;
                j=j.next.next;
            }
            System.out.println(i.data);
        }
	//Implement using Fast and slow pointers
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