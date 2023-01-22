// Time Complexity : O(n)
// Space Complexity : O(1)
// Did this code successfully run on Leetcode : yes
// Any problem you faced while coding this : no

// use slow and fast pointers, fast moves two times forward than slow, 
// by the time fast reaches null slow will have a middle value

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

		@Override
		public String toString() {
			return "Node [data=" + data + ", next=" + next + "]";
		}

	}

	/* Function to print middle of linked list */
	// Complete this function
	void printMiddle() {
		// Write your code here
		// Implement using Fast and slow pointers
		Node slow = head;
		Node fast = head;
		while (fast != null && fast.next != null) {
			slow = slow.next;
			fast = fast.next.next;
		}
		System.out.println("The middle value is: " + slow.data);
	}

	public void push(int newData) {
		Node newNode = new Node(newData);
		newNode.next = head;
		head = newNode;
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
		LinkedList llist = new LinkedList();
		for (int i = 15; i > 0; --i) {
			llist.push(i);
			llist.printList();
			llist.printMiddle();
		}
	}
}