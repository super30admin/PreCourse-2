// Time Complexity :o(n)
// Space Complexity :o(1)
// Did this code successfully run on Leetcode :n/a
// Any problem you faced while coding this :n.a


// Your code here along with comments explaining your approach
//Iterate over linklist and find length of linkedList
//iterate till half of linkedlist and inittialize temp node to head and move temparary node foward.
//once temparary node reached at half of linkedlist, return temparary node
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

    public int getLen(){
        int length =0;
        Node temp = head;
        while(temp!=null){
            length++;
            temp = temp.next;
        }
        return length;
    }
  
    /* Function to print middle of linked list */
   //Complete this function
    void printMiddle() 
    { 
        //Write your code here
	//Implement using Fast and slow pointers
        if(head!=null){
            int length = getLen();
            Node temp = head;
            int middleLength = length/2;
            while(middleLength!=0){
                temp = temp.next;
                middleLength--;
            }
            System.out.println("The middle element is [" + temp.data + "]");
            System.out.println("\n\n");
        }

    } 
  
    public void push(int new_data) 
    { 
        Node new_node = new Node(new_data); 
        new_node.next = head; 
        head = new_node; 
    } 

    public void printList() 
    { 
        Node tnode = head; 
        while (tnode != null) 
        { 
            System.out.print(tnode.data+"->"); 
            tnode = tnode.next; 
        } 
        System.out.println("NULL"); 
    } 
  
    public static void main(String [] args) 
    { 
        LinkedList llist = new LinkedList(); 
        for (int i=15; i>0; --i) 
        { 
            llist.push(i); 
            llist.printList(); 
            llist.printMiddle(); 
        } 
    } 
} 