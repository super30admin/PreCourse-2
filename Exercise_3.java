/**
 * Class representing a linked list
 */
class LinkedList
{ 
    Node head; // head of linked list 

    /**
     * Class represents single node of the linked list
     * This simple contains data field and next filed and a constructor.
     */
    static class Node
    { 
        private int data;
        private Node next; //This is simply a pointer to next node of the linked list
        Node(int data)
        { 
            this.data = data;
            this.next = null;
        } 
    } 
  
    /* Function to print middle of linked list */
    void printMiddle()
    {
        //Implement using Fast and slow pointers
        if (head == null) {
            System.out.println("Empty input list");
        }

        Node slowPointer = head;
        Node fastPointer = head;

        while (fastPointer != null && fastPointer.next != null) {
            fastPointer = fastPointer.next.next;
            slowPointer = slowPointer.next;
        }

        System.out.println(slowPointer.data);

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