/** space complexity: O(1)
 * time complexity: O(n^2)
 * did this code successfully run on Leetcode: This is not a Leetcode problem
 * any problem you faced while coding this: No
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
  
    /**  Function to print middle of linked list 
     * Complete this function
     * This function uses the fast and slow pointer technique to find the middle element of the linked list
     *  The slow pointer moves one step at a time and the fast pointer moves two steps at a time
     *  When the fast pointer reaches the end of the list, the slow pointer will be at the middle element
   */
    void printMiddle() 
    { 
     //Write your code here
	 //Implement using Fast and slow pointers
      Node slow = head;
         Node fast = head;

        if (head != null) {
            while (fast != null && fast.next != null) {
                fast = fast.next.next;
                slow = slow.next;
            }
            System.out.println("The middle element is: " + slow.data);
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
        LinkedList llist = new LinkedList(); 
        for (int i=15; i>0; --i) 
        { 
            llist.push(i); 
            llist.printList(); 
            llist.printMiddle(); 
        } 
    } 
} 