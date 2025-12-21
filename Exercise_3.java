// Time Complexity : O(N) - Need to go through all linked list nodes at least once
// Space Complexity : O(1)
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : No
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
        if (head == null) {
            System.out.println("List is empty!!");
            return;
        }

        if(head.next == null){
            System.out.println(head.data);
            return;
        }

        // Keep 2 points, slow moves one node at a time, fast moves 2 nodes at a time,
        // By the time fast pointer reaches the end of the Linked list, slow pointer covers only half distance and
        // reaches middle.
        Node slow = head;
        Node fast = slow.next.next;
        while(fast != null){
            fast = fast.next;
            if(fast == null) break;
            fast = fast.next;
            slow = slow.next;
        }
        System.out.println(slow.next.data);
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