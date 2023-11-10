// Time Complexity : O(N), Since we are traversing the whole list
// Space Complexity : O(1), Since Constant extra space is used
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : N/A

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
        // Write your code here
        // Implement using Fast and slow pointers
        Node fastPointer = head;
        Node slowPointer = head;

        // Moving the Fast pointer double the times of slow pointer.
        // By the time Fast pointer reaches the end,
        // Slow pointer will be at the half of the point
        // There by Reaching the middle element and printing the data of the middle node
        while (fastPointer != null && fastPointer.next != null) {
            fastPointer = fastPointer.next.next;
            slowPointer = slowPointer.next;
        }
        System.out.print("Middle Element => " + slowPointer.data);

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