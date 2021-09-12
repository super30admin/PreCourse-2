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
        Node slowPointer = head;
        Node fastPointer = head;
         
            while (fastPointer != null && fastPointer.next != null)
            {
                fastPointer = fastPointer.next.next;
                slowPointer = slowPointer.next;
            }
            System.out.println("middle element : "+slowPointer.data + "\n");
         
        //Write your code here
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
        for (int i=1; i>0; --i) 
        { 
            llist.push(i); 
            llist.printList(); 
            llist.printMiddle(); 
        } 
    } 
}

//time complexity : O(N) where n is number of node in list
//space complexity : O(1) space used by each node
//was not difficult only needed to search the syntax to print the value
//was in doubt for edge cases what happens for null or should it give the element itself when has only one element?
//used floyd's algorithm for solving this approach
// Used Floyd's algorithm 
//ran the code and its working anf giving the middle value
