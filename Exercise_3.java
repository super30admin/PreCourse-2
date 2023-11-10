// Time Complexity : O(n), n is the number of nodes.

// Space Complexity : O(1)

// Did this code successfully run on Leetcode : Yes

// Any problem you faced while coding this : No

// Your code here along with comments explaining your approach
/* using the concept of slow and fast pointer, we traverse the linkedlist with slow and fast pointer.
 * move fast twice as fast thann slow. This will help her find the middle node, becuase when fast reaches the end, slow must be at the middle.
 */

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
        Node slow = head;
        Node fast = head;
        while (fast.next != null && fast.next.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }

        System.out.println(slow.data);
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