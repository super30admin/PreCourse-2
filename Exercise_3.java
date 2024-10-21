/*
    Time Complexity : O(n) as slow pointer moves by 1 step and fast moves by 2 steps
            The slow pointer will take approximately n/2 iterations to reach the middle node.
            The fast pointer will traverse the entire list in about n/2 iterations as well,
            since it moves twice as fast.
            Total Traversal: n/2 + n/2 = n

    Space Complexity : O(1) as we are using fixed space pointers = slow and fast and
             no data structures have been used
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
    //Write your code here
	//Implement using Fast and slow pointers

    /*
        First, we will start with both the slow and fast pointers pointing to the head, which is the first element
        then the slow pointer will move by 1 space and fast pointer will move by 2 spaces

        In odd numbers of linked list, at the end, the slow pointer will point to the middle of the list and fast
        pointer will point to the last element {fast.next != null condition will be false}

        In even numbers of linked list, at the end, the slow pointer will point to the second middle element in the list
        and fast pointer will point to NULL {fast != null will be false}
     */

        Node slow = head;
        Node fast = head;

        while (fast != null && fast.next != null)
        {
            slow = slow.next;          // Move slow pointer by 1
            fast = fast.next.next;     // Move fast pointer by 2
        }

        /* this condition {slow != null} is only to ensure one scenario, when the list is empty so slow and fast will be pointing to null
           so while loop condition will fail, so this condition will prevent from Null Pointer Exception
         */
        if (slow != null)
        {
            System.out.println("Middle element is: " + slow.data);
        }
    } 
  
    public void push(int new_data) 
    {
        /*
         eg: 2 -> 4 -> 6 -> 7 -> NULL
         new_node = 8 -> NULL

         new_node.next = head
         8 -> 2 -> 4 -> 6 -> 7 -> NULL
              ↑
             head

         head = new_node
         8 -> 2 -> 4 -> 6 -> 7 -> NULL
         ↑
        head

        */
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