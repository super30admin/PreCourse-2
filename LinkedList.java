package precourse2;
//time complexity: O(n)
//space complexity: O(1)
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
    	Node slow_pointer = head;
        Node fast_pointer = head;   
        System.out.println("slow ptr=" + slow_pointer.data + "\t"); 
        System.out.println("fast ptr=" + fast_pointer.data + "\t"); 
            while (fast_pointer != null && fast_pointer.next != null)
            {
                slow_pointer = slow_pointer.next;
                fast_pointer = fast_pointer.next.next;
                System.out.println("**inside loop:");
                System.out.println("slow ptr=" + slow_pointer.data + "\t");
                if(fast_pointer!=null)
                	System.out.println("fast ptr=" + fast_pointer.data + "\n");
            }
            System.out.println("The middle element is [" +
                                slow_pointer.data + "] \n");    
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