#include<iostream>
using namespace std;  
  

// Time Complexity : O(log n) 
// Space Complexity : O(1) constant space.
// Any problem you faced while coding this : No

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

  struct Node* fast_pointer = head;
  struct Node* slow_pointer = head;

  while(fast_pointer != nullptr && fast_pointer->next != nullptr && fast_pointer->next->next != nullptr)
  {
      fast_pointer = fast_pointer->next->next;
      slow_pointer = slow_pointer->next;
  }

  cout << slow_pointer->data << endl;
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