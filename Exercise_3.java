// Time Complexity : O(N/2)
// Space Complexity : 2 References + N*SizeOf(Node)
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : Odd Even case what happens, which one to show ? ceil or floor rule.
class LinkedList_Custom {
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

        Node fastPtr = head, slowPtr = head;

        int ctr = 0;
        while (fastPtr != null && fastPtr.next != null) {
            System.out.print("[S_" + slowPtr.data + ",F_" + fastPtr.data + "]->");
            slowPtr = slowPtr.next;
            fastPtr = fastPtr.next.next;
        }
        System.out.println("Middle Element : " + slowPtr.data);
    }

    public void push(int new_data) {
        Node new_node = new Node(new_data);
        new_node.next = head;
        head = new_node;
    }

    public void printList() {
        Node tnode = head;
        double ctr = 0;
        while (tnode != null) {
            System.out.print(tnode.data + "->");
            tnode = tnode.next;
            ctr = ctr + 1;
        }

        System.out.println("NULL; /Total Nodes : " + ctr + ", Half : " + Math.ceil(ctr / 2));
    }

    public static void main(String[] args) {
        LinkedList_Custom llist = new LinkedList_Custom();
        for (int i = 15; i > 0; --i) {
            llist.push(i);
            llist.printList();
            llist.printMiddle();
        }
    }
} 