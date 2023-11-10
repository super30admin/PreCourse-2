class LinkedList {
	ListNode head;
	public static class ListNode{
		int data;
		ListNode next;
		ListNode(int data){
			//Initializing Node data
			this.data=data;
			this.next=null;
		}
	}
	
	//Displaying Nodes of List
	void display() {
		ListNode temp=head;
		while(temp!=null) {
			System.out.print(temp.data+"-->");
			temp=temp.next;
		}
		System.out.println("Null");
	}
    void findMidofList() {
    	ListNode slowPtr=head; //move forward with step
    	ListNode fstPtr=head;  //move forward with two steps
    	while(fstPtr!=null && fstPtr.next!=null) {
    		fstPtr=fstPtr.next.next;
    		slowPtr=slowPtr.next;
    	}
    	System.out.print("Middle of singly linked list is \s"+slowPtr.data);
    	}
	public static void main(String[] args) {
		LinkedList h=new LinkedList();
		h.head=new ListNode(20);
		ListNode a=new ListNode(30);
		ListNode b=new ListNode(40);
		ListNode c=new ListNode(50);
		ListNode d=new ListNode(60);
		ListNode e=new ListNode(70);
		h.head.next=a;
		a.next=b;
		b.next=c;
		c.next=d;
		d.next=e;
		e.next=null;
		h.display();
		h.findMidofList();

	}

}
