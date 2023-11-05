// time complexity is O(n) and space is O(1)

class LinkedList {
    constructor() {
        this.head = null; // head of linked list
    }

    /* Linked list node */
    Node = class {
        constructor(d) {
            this.data = d;
            this.next = null;
        }
    }

    push(new_data) {
        let new_node = new this.Node(new_data);
        new_node.next = this.head;
        this.head = new_node;
    }

    printList() {
        let tnode = this.head;
        while (tnode != null) {
            console.log(tnode.data + "->");
            tnode = tnode.next;
        }
        console.log("NULL");
    }

    printMiddle() {
        let slowPtr = this.head;
        let fastPtr = this.head;

        if (this.head != null) {
            while (fastPtr != null && fastPtr.next != null) {
                fastPtr = fastPtr.next.next; // Move fast pointer by two steps
                slowPtr = slowPtr.next; // Move slow pointer by one step
            }

            console.log("The middle element is: " + slowPtr.data);
        }
    }
}

let llist = new LinkedList();
for (let i = 15; i > 0; --i) {
    llist.push(i);
    llist.printList();
    llist.printMiddle();
}
