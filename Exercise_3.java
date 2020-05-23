/*
   Middle Node of Linkedlist
	1)Time Complexity: O(N)
	2)Space Complexity: O(1)
	3)Was able to run successfully on leetcode
	4)No Problem faced during coding the problem 
*/
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
	void printMiddle() {
		// Write your code here
		// Implement using Fast and slow pointers
		Node slow = head; // Intializing slow pointer
		Node fast = head; // Intializing fast pointer

		/*
		 * Traversing through the linkedlist till we reach the last node
		 */
		while (fast != null && fast.next != null) {
			slow = slow.next; // traversing slow pointer by 1 node
			fast = fast.next.next; // traversing fast pointer by 2 nodes
		}
		/*
		 * Printing the value of slow pointer after fast reaches the end
		 */
		System.out.println("The middle element of linkedlist is : " + slow.data);
	}

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

	public static void main(String[] args) {
		LinkedList llist = new LinkedList();
		for (int i = 15; i > 0; --i) {
			llist.push(i);
			llist.printList();
			llist.printMiddle();
		}
	}
}