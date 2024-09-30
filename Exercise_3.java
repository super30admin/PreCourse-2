//time complexity - O(n^2)
//space complexity - O(n)
class LinkedList {
    Node head;

    LinkedList() {
    }

    void printMiddle() {
        if (this.head != null) {
            Node slow_ptr = this.head;

            for(Node fast_ptr = this.head; fast_ptr != null && fast_ptr.next != null; slow_ptr = slow_ptr.next) {
                fast_ptr = fast_ptr.next.next;
            }

        }
    }

    public void push(int new_data) {
        Node new_node = new Node(this, new_data);
        new_node.next = this.head;
        this.head = new_node;
    }

    public void printList() {
        for(Node tnode = this.head; tnode != null; tnode = tnode.next) {
            System.out.print(tnode.data + "->");
        }

        System.out.println("NULL");
    }

    public static void main(String[] args) {
        LinkedList llist = new LinkedList();

        for(int i = 15; i > 0; --i) {
            llist.push(i);
            llist.printList();
            llist.printMiddle();
        }

    }

    class Node {
        int data;
        Node next;

        Node(final LinkedList this$0, int d) {
            this.data = d;
            this.next = null;
        }
    }
}
