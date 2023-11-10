// Time Complexity : Time complexity of printMiddle will be O(n) as the whole linked list is traversed
// Space Complexity : Space Required for printMiddle will be O(1) as no extra space is used except space for the linked list which is O(n)
// Did this code successfully run on Leetcode :Yes
// Any problem you faced while coding this : None

// Your code here along with comments explaining your approach

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
        Node fp = head; // Slow pointer
        Node sp = head; // Fast pointer
        while (fp != null && fp.next != null) { // While slow pointer would move ahead by one element, fast pointer
                                                // would move ahead by 2 elements
            sp = sp.next;
            fp = fp.next.next;
        }
        System.out.println(sp.data);
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