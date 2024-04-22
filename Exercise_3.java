// Time Complexity : O(n log n) where n is the number of elements in the array
// Space Complexity : O(1) as we are not using any extra space
// Did this code successfully run on Leetcode : NA
// Any problem you faced while coding this : No

// Your code here along with comments explaining your approach : The LinkedList class has a Node class that represents a node in the linked list. The printMiddle method finds the middle element of the linked list using the slow and fast pointers. The push method adds a new node to the linked list. The printList method prints the linked list. The main method creates a linked list and prints the middle element of the linked list after adding each element to the linked list.
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
        Node slow = head;
        Node fast = head;
        if (head != null) {
            while (fast != null && fast.next != null) {
                slow = slow.next;
                fast = fast.next.next;
            }
            System.out.println("Middle element is: " + slow.data);
        }
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