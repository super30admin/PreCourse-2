import java.util.function.IntFunction;

import javax.print.event.PrintJobListener;

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
        Node fast_node = head;
        Node slow_node = head;

        if (head != null) {
            while (fast_node != null && fast_node.next != null) {
                fast_node = fast_node.next.next;
                slow_node = slow_node.next;
            }
        }
        System.out.println(slow_node.data);
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