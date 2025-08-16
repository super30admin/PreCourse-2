// Time Complexity: O(n), where n is the number of nodes
// Space Complexity: O(1)
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
	};

	/* Function to print middle of linked list */
	//Complete this function
	printMiddle() {
		//Write your code here
		//Implement using Fast and slow pointers
		if (this.head === null) {
			console.log("NULL");
			return;
		}

		let slow_ptr = this.head;
		let fast_ptr = this.head;

		while (fast_ptr != null && fast_ptr.next != null) {
			slow_ptr = slow_ptr.next;
			fast_ptr = fast_ptr.next.next;
		}

		console.log(`Middle Element is ${slow_ptr.data}`);
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

let llist = new LinkedList();
for (let i = 15; i > 0; --i) {
	llist.push(i);
	llist.printList();
	llist.printMiddle();
}
