// For printMiddle():
// Time Complexity : O(N) , N represents number of items in the LL
// Space Complexity : O(1)

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

        // In case of even lengthed LL's, I will get two elements at the middle. From those, I am returing the first element from those two elements.
        // Overall, I am always returing (0+(length-1))/2 th element from the LL items.
        Node fast = head;
        Node slow = head;
        // To avoid null pointer exceptions, I am safely checking for nulls before performing actions on them.
        while(fast.next!=null && fast.next.next!=null){
            // When fast moves at 2x speed, slow moves 1x.
            fast = fast.next.next;
            slow = slow.next;
        }
        return slow.data;
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