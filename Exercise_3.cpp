// Time Complexity : O(n) but done in one pass like traversal
// Space Complexity :O(1)
// Did this code successfully run on Leetcode :
// Any problem you faced while coding this : 
// in while loop we need to mention fast->next == nullptr to access fast->next->next correctly because it doesnot exist


// Your code here along with comments explaining your approach

#include <iostream>  
using namespace std;  
  
// Struct  
struct Node  
{  
    int data;  
    struct Node* next;  
};  
  
/* Function to get the middle of the linked list*/
void printMiddle(struct Node *head)  
{  
  //YourCode here
  //Use fast and slow pointer technique

  // it is done in one pass 
  // where as finding no of elements and middle of elements again take two passes
  struct Node *slow = head; //travel one node at a time
  struct Node *fast = head; //travel two nodes at a time

  while(fast != nullptr && fast->next != nullptr){// we need to check conditions for fast 
    slow = slow->next;
    fast = fast->next->next;
  }
  if(slow == nullptr){
    cout << "List is Empty" << endl;
  }
  else{
    cout << "middle element is: "<<slow->data << endl;
  }
  

}  
  
// Function to add a new node  
void push(struct Node** head_ref, int new_data)  
{  
    struct Node* new_node = new Node;  
    new_node->data = new_data;  
    new_node->next = (*head_ref);  
    (*head_ref) = new_node;  
}  
  
// A utility function to print a given linked list  
void printList(struct Node *ptr)  
{  
    while (ptr != NULL)  
    {  
        printf("%d->", ptr->data);  
        ptr = ptr->next;  
    }  
    printf("NULL\n");  
}  
  
// Driver Code 
int main()  
{    
    struct Node* head = NULL;  
    printMiddle(head);  
    for (int i=15; i>0; i--)  
    {  
        push(&head, i);  
        printList(head);  
        printMiddle(head);  
    }  
  
    return 0;  
}  