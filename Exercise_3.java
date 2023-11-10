// Time Complexity : O(n)
// Space Complexity : O(1)
// Did this code successfully run on Leetcode :Not found
// Any problem you faced while coding this : No
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

    void printMiddle() {
        // Write your code here
        // Implement using Fast and slow pointers
        if (head != null) {
            Node fast = head, slow = head;
            while (fast != null) {
                if (fast.next == null) {
                    break;
                }
                //fast moves twice as the slow, when fast pointer reaches the end, the slow pointer points the middle
                slow = slow.next;
                fast = fast.next.next;
            }
            System.out.print("The middle element is ["
                    + slow.data + "]");
            System.out.println();
        }
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