// Time Complexity : O(N) -> teh bigger the list, more traversals by the slow and fast pointers. This can be verified by printing out the
// values of slow and fast pointers.
// Space Complexity : O(1) -> Space usage does not increase with incrase in the size of linked list.
// Did this code successfully run on Leetcode :
// Any problem you faced while coding this : Earlier, i was just checking for fastPointer != null in the while loop but then, i updated it to
// fastPOinter.next != null. Then, I went again through the entire algorithm and saw that to avoid null pointer exception, both
// fastPointer and fastPointer.next should not be null.
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
        Node slowPointer = head;
        Node fastPointer = head;
        if (head == null ) {
            System.out.println("Empty list");
            return;
        } else if (head.next == null) {
            System.out.println("Middle of linked list is " + head.data);
            return;
        } else if (head.next.next == null) {
            System.out.println("Middle of linked list is " + head.next.data);
            return;
        } else {
            while(fastPointer != null && fastPointer.next != null ) {
                System.out.println("Fast Pointer " + fastPointer.data);
                System.out.println("Slow Pointer " + slowPointer.data);
                fastPointer = fastPointer.next.next;
                slowPointer = slowPointer.next;
            }
            System.out.println("Middle of the linked list is " + slowPointer.data);
        }
    }

    public void push(int new_data)
    {
        Node new_node = new Node(new_data);
        new_node.next = head;
        head = new_node;
        System.out.println("Head node is " + head.data);
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