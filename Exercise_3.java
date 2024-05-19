// Time Complexity : O (n)
// Space Complexity :O (1)
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this :no

class LinkedLists {
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

        Node current = head; // initialising the head of the list
        if (current == null) { // check to see if there is something in the list
            return;
        }
        if (current.next == null) { // is there are only  2 elements in the list
            System.out.println("Middle of linked list " + current.data);
            return;
        }
    
        Node slow = current; // setting 2 pointers, slow and fast
        Node fast = current;
        while (fast.next != null && fast.next.next != null) {
            slow = slow.next; // iterating slow one by one
            fast = fast.next.next; // iterating fast 2 steps at a time
        }

        System.out.print("MIDDLE: " + slow.data + " ");
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
        LinkedLists llist = new LinkedLists();
        for (int i = 15; i > 0; --i) {
            llist.push(i);
            llist.printList();
            llist.printMiddle();
        }
    }
}