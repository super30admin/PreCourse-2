// Time Complexity : O(N) where N is the number of nodes in linked list
// Space Complexity : O(1) as only constant space pointers are created
// Did this code successfully run on Leetcode : N/A
// Any problem you faced while coding this : No problem. 
// But in case of evenly length linked list, there are two middle nodes,
// I am printing the second one.


// Your code here along with comments explaining your approach
// Initialize two pointers, move first by one step, and second by two steps.
// When second one reaches the end of linkedlist, the first one must be in the middle.

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
    void printMiddle() {
        if(head==null)  return;

        Node slow=head;
        Node fast=head;

        while(slow.next!=null && fast!=null && fast.next!=null){
            slow=slow.next;
            fast=fast.next.next;
        }

        System.out.println(slow.data);
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