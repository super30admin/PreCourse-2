
// Time Complexity : O(n)
// Space Complexity : O(1)

class LinkedList {
    Node head; // head of linked list

    /* Linked list node */
    class Node {
        int data;
        Node next;

        Node(int d) {
            this.data = d;
            this.next = null;
        }
    }

    /* Function to print middle of linked list */
    // Complete this function
    void printMiddle() {
        if (head == null) { // checking if the list is empty. if so printing appropriate message
            System.out.println("Linked List is Empty");
            return;
        }
        // Write your code here
        // Implement using Fast and slow pointers to head
        // Incrementing slow pointer by one step and fast pointer by two steps
        // When fast pointer reaches the end the slow pointer reaches the middle of list
        Node slow = head;
        Node fast = head;
        while (fast.next != null && fast.next.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        System.out.println("Middle of Linked List is : " + slow.data);
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