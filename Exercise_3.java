//Time Complexity : O(n)
//Space Complexity :O(1)
//Did this code successfully run on Leetcode : NA
//Any problem you faced while coding this : got exception while writing condition for
//fast pointer but resolved it quickly.


//Your code here along with comments explaining your approach

class LinkedList 
{ 
 Node head; // head of linked list 

 /* Linked list node */
 class Node 
 { 
     int data; 
     Node next; 
     Node(int d) 
     { 
         data = d; 
         next = null; 
     } 
 } 

 public LinkedList() {
	 head=null;
 }
 /* Function to print middle of linked list */
//Complete this function
 void printMiddle() 
 { 
	 //Write your code here
		//Implement using Fast and slow pointers
	 if(this.head==null) {
		 System.out.println("No elements");
		 return;
	 }
	 if(this.head!=null && this.head.next==null) {
		 System.out.println("Middle element is "+this.head.data);
		 return;
	 }
    
	 Node sp= this.head;
	 Node fp=this.head;
	 
	 while(fp.next!=null && fp.next.next!=null) {
		 sp=sp.next;
		 fp=fp.next.next;
	 }
	
		 System.out.print("Middle of the Linked List is "+sp.data);
	 
	 
 } 

 public void push(int data) 
 { 
     // Create a new node with given data 
     Node NewNode= new Node(data);
 
         if(head==null) {
				head=NewNode;
			}else {
				
				Node temp=head;
				while(temp.next!=null) {
					temp=temp.next;
					
				}
				temp.next=NewNode;
				
			}

 }
	
 public void printList() 
 {  
     // Traverse through the LinkedList 
     // Print the data at current node 
     // Go to next node 
 		Node temp = head;
         while(head!=null) {
			System.out.print(head.data+" ");
			head=head.next;
		}
		System.out.println();
		head=temp;
 } 

 public static void main(String [] args) 
 { 
     LinkedList llist = new LinkedList(); 
     for (int i=15; i>0; --i) 
     { 
         llist.push(i); 
         System.out.println("\nlist is");
         llist.printList(); 
        
        llist.printMiddle(); 
     } 
 } 
} 