// Time Complexity : O(n)
// Space Complexity : O(1)
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : Referred some documention and videos and coded

class LinkedList {
    Node head; // head of linked list

    /* Linked list node */
    class Node {
        int data;
        Node next;

        Node(int d) {
            data = d;
            next = null;
        }
    }

    /* Function to print middle of linked list */
    // Complete this function
    void printMiddle() {
        // Start both slow and fast pointer from head
        Node slp = head;
        Node fp = head;

        while (fp != null && fp.next != null) {
            // Increment fast pointer by 2 till last element
            fp = fp.next.next;
            // Increment slow pointer by 1
            slp = slp.next;

        }
        // As soon as the fast pointer reaches the end, the slow pointer will reach at
        // the mid position
        System.out.println("Middle " + slp.data);
    }

    public void push(int new_data) {
        Node new_node = new Node(new_data);
        new_node.next = head;
        head = new_node;
    }

    public void printList() {
        Node tnode = head;
        while (tnode != null) {
            System.out.print(tnode.data + "->");
            tnode = tnode.next;
        }
        System.out.println("NULL");
    }

    public static void main(String[] args) {
        LinkedList llist = new LinkedList();
        for (int i = 15; i > 0; --i) {
            llist.push(i);
            llist.printList();
            llist.printMiddle();
        }
    }
}