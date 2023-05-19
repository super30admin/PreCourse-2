//Time Complexity for Push operations is O(1). While print operations have time Complexity of O(n)
// Space Complexity is O(n)

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
        // Assuming the second node will be the middle node if the input is of even
        // length(as given on leet code)
        Node slowPtr = head;
        Node fastPtr = head;

        if (head != null) {
            while (fastPtr != null && fastPtr.next != null) {
                fastPtr = fastPtr.next.next;
                slowPtr = slowPtr.next;
            }
            System.out.println("Middle element: " + slowPtr.data);
        }

        // // Assuming that first element is the middle one for even length input
        // Node slowPtr = head;
        // Node fastPtr = head;
        // Node prevSlowPtr = null;

        // if (head != null) {
        // while (fastPtr != null && fastPtr.next != null) {
        // fastPtr = fastPtr.next.next;
        // prevSlowPtr = slowPtr;
        // slowPtr = slowPtr.next;
        // }
        // if (fastPtr == null) {
        // System.out.println("Middle element: " + prevSlowPtr.data);
        // } else {
        // System.out.println("Middle element: " + slowPtr.data);
        // }
        // }

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