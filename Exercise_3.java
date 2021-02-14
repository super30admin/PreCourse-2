package precourse2;

class FindMidPointOfSonglyLinkedList 
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
    	Node slowPtr = head;
    	Node fastPtr = head;
    	
    	if(head != null) {
    		while(fastPtr != null && fastPtr.next != null) {
    			fastPtr = fastPtr.next.next;
    			slowPtr = slowPtr.next;
    		}
    		System.out.println("Middle element in this linked list is: "+slowPtr.data);
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
    	FindMidPointOfSonglyLinkedList llist = new FindMidPointOfSonglyLinkedList(); 
        for (int i=15; i>0; --i) 
        { 
            llist.push(i); 
            //llist.printList(); 
        } 
        llist.printMiddle(); 
    } 
} 