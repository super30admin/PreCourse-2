// Time Complexity: O(n) — We traverse the list only once using two pointers
// Space Complexity: O(1) — No extra space is used, only pointers

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

    /* Function to print the middle of the linked list */
    void printMiddle() {
        if (head == null) {
            System.out.println("The list is empty.");
            return;
        }

        Node slow = head;
        Node fast = head;

        // Move fast pointer 2 steps and slow pointer 1 step at a time
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }

        // When fast reaches end, slow is at the middle
        System.out.println("Middle element is [" + slow.data + "]");
    }

    // Function to push a new node at the beginning
    public void push(int new_data) {
        Node new_node = new Node(new_data);
        new_node.next = head;
        head = new_node;
    }

    // Function to print the linked list
    public void printList() {
        Node tnode = head;
        while (tnode != null) {
            System.out.print(tnode.data + "->");
            tnode = tnode.next;
        }
        System.out.println("NULL");
    }

    // Driver method
    public static void main(String[] args) {
        LinkedList llist = new LinkedList();
        for (int i = 15; i > 0; --i) {
            llist.push(i);
            llist.printList();
            llist.printMiddle();
        }
    }
}
