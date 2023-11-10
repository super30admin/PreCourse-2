/*
Time complexity:
Space Complexity:
Did this code successfully run on Leetcode:
Any problem you faced while coding this: 

Code along with comments explaining my approach is as follows
*/

class LinkedList {
    Node head; // head of linked list
    static int n = 0;

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
        // Method 1
        Node slow_pointer = head;
        Node fast_pointer = head;
        while (fast_pointer != null && fast_pointer.next != null) {
            fast_pointer = fast_pointer.next.next;
            slow_pointer = slow_pointer.next;
        }
        System.out.println("Fast/Slow pointer method: Middle Element is " +
                slow_pointer.data + "");

        // Method 2
        Node tmp = head;
        for (int i = 0; i < n / 2; i++) {
            tmp = tmp.next;
        }
        System.out.println("Middle Element is " + tmp.data + "\n");

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
            n++;
            llist.printList();
            llist.printMiddle();
        }

    }
}