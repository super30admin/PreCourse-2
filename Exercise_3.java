
// Time Complexity :O(logn)
// Space Complexity :O(n)
// Any problem you faced while coding this : None


// Your code here along with comments explaining your approach
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
  
    /* Function to print middle of linked list */
   //Complete this function
    void printMiddle() 
    { 
        // Create two pointers slow and fast
        Node slow= head;
        Node fast=head;
        // if only one element is present print that
        if (head.next==null){
            System.out.println(head.data);

        }// if two elements are present, print first element 
        else if (head.next.next==null){
            System.out.println(head.data);

        }// otherwise, increment fast pointer twice the slow pointer 
        else{
            while(fast.next!= null && fast.next.next!= null){

                slow=slow.next;
                fast=fast.next.next;
            }
            // when fast cannot be incremented, slow will be at mid
            
        }

       
        
        System.out.println(slow.data);
        //Write your code here
	//Implement using Fast and slow pointers
    } 
  
    public void push(int new_data) 
    { 
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