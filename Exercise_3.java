class Exercise_3 {
    Node head; // head of linked list

    /*
     * Time complexity to Middle Element in SLL is O(n).
     *
     * Space complexity will be O(1)
     */
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
        if (head == null || head.next == null) {
            System.out.println(head.data);
        }
        // Write your code here
        // Implement using Fast and slow pointers
        Node ptr1 = head;
        Node ptr2 = head;

        while (ptr2.next != null && ptr2.next.next != null) {
            ptr1 = ptr1.next;
            ptr2 = ptr2.next.next;
        }

        System.out.println(ptr1.data);
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
        Exercise_3 llist = new Exercise_3();
        for (int i = 15; i > 0; --i) {
            llist.push(i);
            llist.printList();
            llist.printMiddle();
        }
    }
}