#include<bits/stdc++.h>  
using namespace std;  
  
// Struct  
struct Node  
{  
    int data;  
    struct Node* next;  
};  
//TC : O(n) n is the size of LL
//SC : O(1)  
/* Function to get the middle of the linked list*/
void printMiddle(struct Node *head)  
{  
  //YourCode here
  struct Node* slow = head;
  struct Node* fast = head;
  while(fast!=nullptr && fast->next!=nullptr){
    fast=fast->next->next;//move the fast pointer 2 times more than the slow 
    slow=slow->next;
  }
  //print the middle element in the linked list
  cout << "The middle of the linked list/n" <<  slow->data << endl;
  //Use fast and slow pointer technique
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