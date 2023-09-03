class LinkedList 
{ 
    Node head; // head of linked list 
    int counter=0;

    /* Linked list node */
     // Class Node used to create a Node whenever new element is added.
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
   // Time complexity O(n/2)
    void printMiddle() 
    { 
        if (counter ==0 || head == null)
        {
          System.out.println("List is empty");
          return;
        }
        
        //System.out.println(counter);
        int mid = counter/2;
        Node temp = head;
        if(temp.next==null)
        {
            System.out.println(temp.data);
            return;
        }
        for(int i=0;i<mid;i++)
        {
            temp = temp.next;
        } 

        System.out.println(temp.data);

        //Write your code here
	//Implement using Fast and slow pointers
    } 
  
    // Method to push/ insert element in the Linked List
    public void push(int new_data) 
    { 
        Node new_node = new Node(new_data); 
        new_node.next = head; 
        head = new_node; 
        counter+=1;
    } 

    // Print Linked List 
    // Time complexity: O(n) where n is number 
    //of elements in the Linked List
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


  // Driver code
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