//Problem 3: Mid point of Singly Linked list

//   Time Complexity : The worst time complexity for this problem is O(n/2) As we use double pointer, we can find the mid element in n/2 traversal
//   Space Complexity : The space complexity for this problem would be O(n+n) as we have 2 pointers
//   Any problem you faced while coding this : No


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
        //Write your code here
        //Implement using Fast and slow pointers
        Node temp1, temp2 = null;
        if(head == null)
            System.out.println("There is no node");
        else{
            temp1 = head;
            temp2 = head;
            while(temp1!= null) {
                if(temp1.next == null){
                    temp1=temp1.next;
                }
                else{
                    temp1 = temp1.next.next;
                    temp2 = temp2.next;
                }
            }
            System.out.println(temp2.data);
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