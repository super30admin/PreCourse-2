  //Please read sample.java file before starting.
  //Kindly include Time and Space complexity at top of each file
class LinkedList {
    constructor() {
        this.head = null; // head of linked list
    }

    /* Linked list node */
    static Node = class {
        constructor(d) {
            this.data = d;
            this.next = null;
        }
    }

    /* Function to print middle of linked list */
    printMiddle() {
        //Write your code here
        //Implement using Fast and slow pointers
    }

    push(new_data) {
        let new_node = new LinkedList.Node(new_data);
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
}

// Driver code
let llist = new LinkedList();
for (let i = 15; i > 0; --i) {
    llist.push(i);
    llist.printList();
    llist.printMiddle();
}