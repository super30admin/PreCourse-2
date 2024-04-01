/* Time Complexity : O(n)
// Space Complexity :O(1)
// Did this code successfully run on Leetcode :yes
// Any problem you faced while coding this :no


// Your code here along with comments explaining your approach*/
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
        if(head == null){
            return;
        }
        if(head.next == null){
            System.out.println("Middle of linked list "+ head.data);

            return;
        }
        Node fast = head;
        Node slow = head;

        while(fast != null && fast.next !=null){
            slow = slow.next;
            fast = fast.next.next;
        }
        System.out.println("Middle of linked list "+ slow.data);
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
/*Output:
 * 15->NULL
Middle of linked list 15
14->15->NULL
Middle of linked list 15
13->14->15->NULL
Middle of linked list 14
12->13->14->15->NULL
Middle of linked list 14
11->12->13->14->15->NULL
Middle of linked list 13
10->11->12->13->14->15->NULL
Middle of linked list 13
9->10->11->12->13->14->15->NULL
Middle of linked list 12
8->9->10->11->12->13->14->15->NULL
Middle of linked list 12
7->8->9->10->11->12->13->14->15->NULL
Middle of linked list 11
6->7->8->9->10->11->12->13->14->15->NULL
Middle of linked list 11
5->6->7->8->9->10->11->12->13->14->15->NULL
Middle of linked list 10
4->5->6->7->8->9->10->11->12->13->14->15->NULL
Middle of linked list 10
3->4->5->6->7->8->9->10->11->12->13->14->15->NULL
Middle of linked list 9
2->3->4->5->6->7->8->9->10->11->12->13->14->15->NULL
Middle of linked list 9
1->2->3->4->5->6->7->8->9->10->11->12->13->14->15->NULL
Middle of linked list 8
 */
