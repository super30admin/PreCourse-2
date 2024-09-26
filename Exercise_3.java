/**
 * Time Complexity : O(n / 2)
 * Space Complexity: O(1)
 * Did this code successfully run on Leetcode : Yes, https://leetcode.com/problems/middle-of-the-linked-list/
 *
 * Any problem you faced while coding this : NA
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
    //Complete this function
    void printMiddle() {
        //Write your code here
        //Implement using Fast and slow pointers

        Node slow = head;
        Node fast = head;
        while (fast != null && fast.next != null) {
            fast = fast.next.next;
            slow = slow.next;
        }
        System.out.println(slow.data);

        /* Simple brute force
        int count = 0;
        Node node = head;
        while (node != null) {
            count++;
            node = node.next;
        }
        node = head;
        int i = 0;
        while (i < count / 2) {
            i++;
            node = node.next;
        }
        System.out.println(node.data);*/

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