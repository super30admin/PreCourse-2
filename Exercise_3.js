

class Node {
    constructor(val) {
        this.val = val;
        this.next = null;
    }
}

class LinkedList {
    constructor() {
        this.head = null;
        this.tail = null;
        this.length = 0;
    }


    //Inserts value at the end
    //O(1)
    push(val) {
        let newNode = new Node(val);
        if (!this.head) {
            this.head = newNode;
            this.tail = newNode;
        } else {
            this.tail.next = newNode;
            this.tail = newNode;
        }
        this.length++;
        return this;

    }

    //Finds the middle elemnt in the linked list
    //Using two pointers technique
    // O(n)
    printMiddle() {

        let pointer1 = this.head;
        let pointer2 = this.head;
        if (this.head) {
            while (pointer2 && pointer2.next !== null) {
                pointer2 = pointer2.next.next;
                pointer1 = pointer1.next;
            }
            return pointer1.value;
        }

    }


    //     Print all the values in the list
    //O(n)
    printList() {
        let currentNode = this.head;
        let list = [];
        while (currentNode) {
            list.push(currentNode.val);
            currentNode = currentNode.next;
        }

        return list;
    }


}

let ll = new LinkedList();
ll.push(10);
ll.push(20);
ll.push(30);
ll.push(50);
ll.find(20);
ll.push(60);
ll.push(86);
ll.printMiddle(); //prints 50