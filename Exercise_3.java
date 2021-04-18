// Time Complexity : O(n) - Traverse till end of list
// Space Complexity : O(1) - 2 pointers for existing memory head node
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
        //Implement using Fast and slow pointers
        Node slow=head;
        Node fast=head;

        if(head!=null) {  // Edge case check if linkedlist is not null
            while (fast != null && fast.next!=null) { // Check if faster pointer and its next node are not null

                slow = slow.next;               // move slow pointer by one step
                fast = fast.next.next;          // move fast pointer double faster than slow so slow pointer will be in the middle
                // when fast pointer finished traversal
            }
            System.out.println("Middle element is "+slow.data); // Print middle element
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