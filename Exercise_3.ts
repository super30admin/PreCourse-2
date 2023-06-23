
class MyNode { 
    data: number;
    next: MyNode ;

    constructor(d: number) {
        this.data = d;
        this.next;
    }
}
class LinkedList {
    head: MyNode |any ;

    constructor() {
        this.head= null;
    }

    printMiddle(): void {
        let slow: any = this.head ;
        let fast = this.head;

        //as soon as the fast pointer 
        //reaches the middle of the list our slow pointer 
        //will point to middle element
        //fast= 2slow
        if (this.head !== null) {
            while (fast !== null && fast.next !== null) {
                fast = fast.next.next;
                slow = slow.next;
            }
            console.log("The middle element is [" + slow.data + "]\n");
        }
    }

    push(new_data: number): void {
        let new_node = new MyNode(new_data);
        new_node.next = this.head;
        this.head = new_node;
    }

    printList(): void {
        let tnode = this.head;
        while (tnode !== null) {
            console.log(tnode.data + "->");
            tnode = tnode.next;
        }
        console.log("NULL");
    }
}


let llist = new LinkedList();
for (let i = 15; i > 0; --i) {
    llist.push(i);
    llist.printList();
    llist.printMiddle();
}
