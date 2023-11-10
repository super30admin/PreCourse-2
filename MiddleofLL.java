///Time and space complexity
//Time Complexity: O(n)
//Space Complexity: O(1)
package Precourse2;
public class MiddleofLL {
		Node head;
		class Node {
			int data;
			Node next;
			public Node(int data)
			{
				this.data = data;
				this.next = null;
			}
		}
		public void pushNode(int data)
		{
			Node new_node = new Node(data);
			new_node.next = head;
			head = new_node;
		}
		public void printNode()
		{
			Node temp = head;
			while (temp != null) {
				System.out.print(temp.data + "->");
				temp = temp.next;
			}
			System.out.print("Null"+"\n");
		}
		public int getLen()
		{
			int length = 0;
			Node temp = head;
			while (temp != null) {
				length++;
				temp = temp.next;
			}
			return length;
		}
		public void printMiddle()
		{
			if (head != null) {
				int length = getLen();
				Node temp = head;
				int middleLength = length / 2;
				while (middleLength != 0) {
					temp = temp.next;
					middleLength--;
				}
				System.out.print("The middle element is ["
								+ temp.data + "]");
				System.out.println();
			}
		}

		public static void main(String[] args)
		{
			MiddleofLL list = new MiddleofLL();
			for (int i = 10; i >= 1; i=i-2) {
				list.pushNode(i);
			}
			list.printNode();
			list.printMiddle();
		}
}