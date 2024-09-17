// Time Complexity : O(n)
// Space Complexity : O(1)
// Did this code successfully run on Leetcode : 
// Any problem you faced while coding this : No

public class Exercise_3 {
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
	void printMiddle() {
		// Use 2 pointer approach. 
		// The fastPtr jumps 2 nodes, and the slowPtr moves to the next node after each iteration.
		// The middle element will be in the slowPtr.
		if (this.head == null) {
			System.out.println("Linked list is empty.");
		}
		Node fastPtr = this.head;
		Node slowPtr = this.head;

		while (fastPtr != null && fastPtr.next != null) {
			fastPtr = fastPtr.next.next;
			slowPtr = slowPtr.next;
		}
		System.out.println("Middle Element of Linked List = " + slowPtr.data);
	}

	public void push(int new_data) {
		// Insert data to the  beginning of the linked list
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
		Exercise_3 llist = new Exercise_3();
		for (int i = 15; i > 0; --i) {
			llist.push(i);
			llist.printList();
			llist.printMiddle();
		}
	}
}