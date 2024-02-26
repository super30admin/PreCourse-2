class LinkedList

/*
 * for the printMiddle() function:
The Time Complexity is O(n), as it needs to traverse part of the list proportional to its size to find the middle.
The Space Complexity is O(1), due to the constant amount of extra space used, regardless of the list size.

OutPut:
15->NULL
The middle element is [15]
14->15->NULL
The middle element is [15]
13->14->15->NULL
The middle element is [14]
12->13->14->15->NULL
The middle element is [14]
11->12->13->14->15->NULL
The middle element is [13]
10->11->12->13->14->15->NULL
The middle element is [13]
9->10->11->12->13->14->15->NULL
The middle element is [12]
8->9->10->11->12->13->14->15->NULL
The middle element is [12]
7->8->9->10->11->12->13->14->15->NULL
The middle element is [11]
6->7->8->9->10->11->12->13->14->15->NULL
The middle element is [11]
5->6->7->8->9->10->11->12->13->14->15->NULL
The middle element is [10]
4->5->6->7->8->9->10->11->12->13->14->15->NULL
The middle element is [10]
3->4->5->6->7->8->9->10->11->12->13->14->15->NULL
The middle element is [9]
2->3->4->5->6->7->8->9->10->11->12->13->14->15->NULL
The middle element is [9]
1->2->3->4->5->6->7->8->9->10->11->12->13->14->15->NULL
The middle element is [8]
 */
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
        Node fast = head;
        Node slow = head;
        
        if (head != null){
            while (fast != null && fast.next != null) {
                fast = fast.next.next;
                slow = slow.next;
                
            }
            System.out.println("The middle element is [" + slow.data + "]");
        }
        //Write your code here
	//Implement using Fast and slow pointers
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