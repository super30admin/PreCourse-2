/* 
print middle works on O(n) beacuse the pointers go through list once  
*/


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

        //using two pointers, one fast and one slow 
        Node fast = head ; 
        Node slow = head ; 


        while (fast.next != null && fast.next.next != null) {
            //so, fast takes two steps at a time and slow takes one. This means when fast hit null, the slow will be half the way
            fast = fast.next.next ; 
            slow = slow.next ; 
        }

        //printing the middle value 
        System.out.println("this is the middle element " + slow.data) ; 
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