/*

TC: O(n)
SC: O(1)
Logic:
The way slow and fast pointers move, slow always ends up travelling half of fast. Hence we are able to reach mid in one traversal, and we stop when fast has made the last jump.

*/

#include<bits/stdc++.h>  
#include<iostream>
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
    //Not specified what to do when even, so assuming input to be odd.
  //Use fast and slow pointer technique
  if(head == NULL)  return;
  Node* fast = head;    Node* slow = head;
  while(fast->next && fast->next->next) slow = slow->next, fast = fast->next->next;
  cout<<slow->data<<endl;
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