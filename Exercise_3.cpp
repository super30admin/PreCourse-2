#include<bits/stdc++.h>  
using namespace std;  
  
// Struct  
struct Node  
{  
    int data;  
    struct Node* next;  
};  
  
/* Function to get the middle of the linked list*/
// Time Complexity : O(n)
// Space Complexity : O(1)

/* Increment fast pointer by two locations and slow pointer by one location
*  until slow pointer reaches to end of linked list.
*/
void printMiddle(struct Node *head)  
{  
  //YourCode here
  //Use fast and slow pointer technique

  if (head == NULL)
    return;

  Node *fastPointer, *slowPointer;
  
  slowPointer = fastPointer = head;
  while (fastPointer->next != NULL && fastPointer->next->next != NULL)
  {
      slowPointer = slowPointer->next;
      fastPointer = fastPointer->next->next;
  }
  
  printf("Middle element is : %d \n\n", slowPointer->data);
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
    for (int i=15; i>0; i--)  
    {  
        push(&head, i);  
        printList(head);  
        printMiddle(head);  
    }  
  
    return 0;  
}  