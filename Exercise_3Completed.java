class LinkedList { 
    Node head; // head of linked list
  
    /* Linked list node */
    class Node { 
        int data; 
        Node next; 
        Node(int d) { 
            data = d; 
            next = null; 
        } 
    } 
  
    /* Function to print middle of linked list */
    void printMiddle() { 
        // Initialize two pointers, slow and fast
        Node slow_ptr = head; 
        Node fast_ptr = head; 

        // Move fast_ptr by two nodes and slow_ptr by one node until fast_ptr reaches the end
        while (fast_ptr != null && fast_ptr.next != null) { 
            fast_ptr = fast_ptr.next.next; 
            slow_ptr = slow_ptr.next; 
        } 

        // slow_ptr now points to the middle node
        if (slow_ptr != null) {
            System.out.println("The middle element is [" + slow_ptr.data + "]"); 
        }
    } 
  
    /* Function to push a new node to the front of the linked list */
    public void push(int new_data) { 
        Node new_node = new Node(new_data); // Create a new node
        new_node.next = head; // Link the old list off the new node
        head = new_node; // Move the head to point to the new node
    } 

    /* Function to print the linked list */
    public void printList() { 
        Node tnode = head; // Initialize a temporary node
        while (tnode != null) { 
            System.out.print(tnode.data + "->"); // Print the data of each node
            tnode = tnode.next; // Move to the next node
        } 
        System.out.println("NULL"); 
    } 
  
    public static void main(String [] args) { 
        LinkedList llist = new LinkedList(); 
        for (int i = 15; i > 0; --i) { 
            llist.push(i); // Push new data to the front of the list
            llist.printList(); // Print the list
            llist.printMiddle(); // Print the middle of the list
        } 
    } 
} 
