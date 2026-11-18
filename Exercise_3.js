// Time: O(n); Space: O(1)

class LinkedList {
    constructor() {
        this.head = null;
    }

    static Node = class {
        constructor(data) {
            this.data = data;
            this.next = null;
        }
    };

    // For even lengths, the fast/slow traversal selects the second middle.
    printMiddle() {
        if (this.head === null) {
            console.log("The list is empty.");
            return;
        }

        let slow = this.head;
        let fast = this.head;
        while (fast !== null && fast.next !== null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        console.log("The middle element is " + slow.data);
    }

    push(newData) {
        const newNode = new LinkedList.Node(newData);
        newNode.next = this.head;
        this.head = newNode;
    }

    printList() {
        const values = [];
        let current = this.head;
        while (current !== null) {
            values.push(current.data);
            current = current.next;
        }
        console.log(values.join("->") + (values.length ? "->" : "") + "NULL");
    }
}

const list = new LinkedList();
for (let i = 15; i > 0; --i) {
    list.push(i);
    list.printList();
    list.printMiddle();
}
