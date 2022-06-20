// Time Complexity :O(n)
// Space Complexity :O(n)
// Did this code successfully run on Leetcode :
// Any problem you faced while coding this :
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
        Node currNode = head;
        int length=0;
        while(currNode.next !=null){
            currNode = currNode.next;
            length++;
        }
        currNode = head;
        for(int i=0;i<length/2;i++){
            currNode = currNode.next;
        }
        System.out.println("Execise 3: The middle element in LinkedList is: " + currNode.data);
    } 
  
    public void push(int new_data) 
    { 
        Node new_node = new Node(new_data);
        if(head == null){
            head = new_node;
        }else{
            Node currNode = head;
            while(currNode.next != null){
                currNode = currNode.next;
            }
            currNode.next = new_node;
        }
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
  
//    public static void main(String [] args)
//    {
//        LinkedList llist = new LinkedList();
//        for (int i=15; i>0; --i)
//        {
//            llist.push(i);
//            llist.printList();
//            llist.printMiddle();
//        }
//    }
} 